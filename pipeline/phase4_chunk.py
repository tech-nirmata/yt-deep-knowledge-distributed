#!/usr/bin/env python3
"""
Phase 4 chunk processor — runs on a single GitHub Actions runner.
Reads queue/phase4-remaining.tsv, processes its slice based on CHUNK_INDEX
and TOTAL_CHUNKS env vars, outputs results to results/<chunk>/.

KEY ROTATION (no compromise on quality):
  - Chunk receives ALL keys via GEMINI_KEYS_JSON env var (preferred)
  - Falls back to single-key GEMINI_API_KEY for backward compat
  - For each video, rotates through (key, model) combos until one succeeds
  - Per-chunk circuit breaker tracks dead (key, model) combos to avoid retrying exhausted slots
  - Starting offset = CHUNK_INDEX % len(keys) → distributes load across chunks
"""
from __future__ import annotations  # PEP 604 X|None syntax usable on py3.9
import os, sys, time, json, signal, hashlib
from pathlib import Path
from google import genai
from google.genai import types as gtypes, errors as gerrors

CHUNK = int(os.environ["CHUNK_INDEX"])
TOTAL = int(os.environ["TOTAL_CHUNKS"])
# Multi-account partitioning: each GitHub account processes a disjoint HALF of the
# queue so two accounts' 20-job pools ~2x throughput with ZERO duplicate work.
# Backward compatible: NUM_HALVES=1 + HALF=0 (defaults) → original whole-queue behavior.
HALF = int(os.environ.get("HALF", "0"))
NUM_HALVES = int(os.environ.get("NUM_HALVES", "1"))

# Multi-key rotation: prefer GEMINI_KEYS_JSON, fall back to GEMINI_API_KEY
_KEYS_JSON = os.environ.get("GEMINI_KEYS_JSON", "").strip()
if _KEYS_JSON:
    try:
        ALL_KEYS = json.loads(_KEYS_JSON)
        if not isinstance(ALL_KEYS, list) or not ALL_KEYS:
            raise ValueError("GEMINI_KEYS_JSON must be a non-empty array")
    except (json.JSONDecodeError, ValueError) as e:
        print(f"FATAL: invalid GEMINI_KEYS_JSON: {e}", flush=True)
        sys.exit(2)
else:
    _single = os.environ.get("GEMINI_API_KEY", "").strip()
    if not _single:
        print("FATAL: neither GEMINI_KEYS_JSON nor GEMINI_API_KEY set", flush=True)
        sys.exit(2)
    ALL_KEYS = [_single]

QUEUE = Path("queue/phase4-remaining.tsv")
OUT_DIR = Path(f"results/chunk-{CHUNK:02d}")
OUT_DIR.mkdir(parents=True, exist_ok=True)
LOG = OUT_DIR / "_chunk.log"

PROMPT = """CRITICAL: The viewer ALREADY HAS THE FULL TRANSCRIPT. Do NOT transcribe, paraphrase, or quote spoken audio. Write ONLY about visible content the transcript cannot capture. Capture EVERYTHING visible — do not skip details. EVERY on-screen text, EVERY chart, EVERY slide, EVERY meaningful B-roll moment.

Required output (markdown sections):

## Setting & production
Location, camera angle, wardrobe, props, lighting, background. Note any change in setting throughout the video.

## Timestamped visual events (EVERY visual change)
ONLY non-audio content. Each entry: `MM:SS — what appears on screen`. Include EVERY:
- On-screen text overlay, lower third, caption, kinetic typography (verbatim)
- Slide change, chart, graph, diagram, flowchart, table
- Screen recording (name the app + the action shown step by step)
- B-roll, cutaway, stock footage, archival clip
- Whiteboard, notepad, sketch (describe content)
- Demo, product walkthrough, screen-share, dashboard
- Before/after comparison, results screenshot
- Cut/transition that changes scene
- Animation or motion graphic

## All visual frameworks
EVERY diagram, model, framework, matrix, pyramid, funnel, quadrant, flowchart shown. Describe structure + labels in enough detail to reconstruct. Capture all of them, not just the main one.

## Brand & reference visual evidence
EVERY URL, social handle, brand logo, product name, software UI, book cover, business card visible on screen. List exhaustively.

## Visual storytelling devices
Pattern interrupts, zoom-ins, fast cuts, slow pans, color shifts, lower-third reveals — only when they change meaning.

## Speaker body-language peaks
Distinctive moments where energy or gesture significantly changes meaning. Skip routine gestures.

If video is truly talking-head with zero meaningful visuals beyond speaker's face: write a single sentence saying so and stop."""

# Per-process global state for circuit breakers
# _cooldown_until[(key_idx, model)] = unix-ts to skip until.
# Per-minute Gemini RPM limits heal in 60s, so we use a 90s cooldown after N 429s.
# Per-day RPD limits don't heal within the chunk run, but if cooldown re-tests
# get hit again immediately, the cooldown re-extends — natural backoff.
_cooldown_until = {}
_429_combo_count = {}  # rolling count per (key,model); resets on success
MAX_COMBO_429 = 2  # after this many consecutive 429s, enter cooldown
COOLDOWN_S = 90  # seconds to skip a (key, model) after MAX_COMBO_429
# Free quota is per-MODEL-per-project-per-day, so EACH model id is a separate daily bucket.
# Rotating more model ids = more daily capacity on the SAME keys (no new keys/accounts/bans).
# Ordered best→fallback so every video gets the strongest model that still has quota (no quality
# compromise); cooldown breaker drops to the next only when one is exhausted. All are multimodal
# and accept a YouTube URL server-side (verified gemini-3.1-flash-lite live). 2.0 family excluded
# to hold quality. 4 flash + 4 flash-lite = 8 buckets ≈ 2x the old 4-model capacity.
MODELS = [
    "gemini-2.5-flash",            # proven workhorse, strong + fast
    "gemini-3.5-flash",            # newest flagship flash
    "gemini-3-flash-preview",      # high quality (slower; lower priority)
    "gemini-flash-latest",         # alias → current flash
    "gemini-3.1-flash-lite",       # verified: YouTube video, 9s, accurate
    "gemini-2.5-flash-lite",
    "gemini-flash-lite-latest",
    "gemini-3.1-flash-lite-preview",
]
FPS = 1.0

# Reusable client cache: api_key -> genai.Client
_client_cache = {}


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')} c{CHUNK}] {msg}"
    print(line, flush=True)
    with LOG.open("a") as f:
        f.write(line + "\n")


def get_client(api_key: str) -> "genai.Client":
    if api_key not in _client_cache:
        _client_cache[api_key] = genai.Client(api_key=api_key)
    return _client_cache[api_key]


def in_cooldown(key_idx: int, model: str) -> bool:
    """True if this (key, model) is in cooldown right now."""
    until = _cooldown_until.get((key_idx, model), 0)
    return time.time() < until


def mark_cooldown(key_idx: int, model: str, key_suffix: str):
    """Put (key, model) in cooldown for COOLDOWN_S seconds."""
    _cooldown_until[(key_idx, model)] = time.time() + COOLDOWN_S
    _429_combo_count[(key_idx, model)] = 0  # reset count; will re-trip if cooldown wasn't enough
    log(f"  COOLDOWN key=***{key_suffix} model={model} ({MAX_COMBO_429}+ quota) — skip {COOLDOWN_S}s")


def all_models_cooling(model: str) -> bool:
    """True if every key has this model cooling down."""
    return all(in_cooldown(i, model) for i in range(len(ALL_KEYS)))


def all_combos_cooling() -> bool:
    """True if every (key, model) combo is cooling down."""
    now = time.time()
    return all(
        _cooldown_until.get((i, m), 0) > now
        for i in range(len(ALL_KEYS))
        for m in MODELS
    )


def min_cooldown_wait() -> float:
    """Seconds until the earliest cooldown expires (>=0). Used when all combos cooling."""
    now = time.time()
    earliest = min(
        _cooldown_until.get((i, m), now)
        for i in range(len(ALL_KEYS))
        for m in MODELS
    )
    return max(0.0, earliest - now)


def try_video(url: str, vid: str, start_key_idx: int) -> tuple[str | None, str | None]:
    """
    Try to analyze video. Rotates through (key, model) combos.
    Returns (result_text, used_model_label) or (None, None) on total failure.

    Strategy: for each MODEL (priority order), try each key starting from start_key_idx.
    Within a (key, model), retry up to 3 times on transient errors.
    Mark (key, model) dead after MAX_COMBO_429 quota errors.
    """
    n_keys = len(ALL_KEYS)
    for model in MODELS:
        if all_models_cooling(model):
            continue
        for key_offset in range(n_keys):
            key_idx = (start_key_idx + key_offset) % n_keys
            if in_cooldown(key_idx, model):
                continue
            api_key = ALL_KEYS[key_idx]
            key_suffix = api_key[-6:]
            client = get_client(api_key)
            for retry in range(3):
                try:
                    resp = client.models.generate_content(
                        model=model,
                        contents=gtypes.Content(parts=[
                            gtypes.Part(
                                file_data=gtypes.FileData(file_uri=url, mime_type="video/mp4"),
                                video_metadata=gtypes.VideoMetadata(fps=FPS),
                            ),
                            gtypes.Part(text=PROMPT),
                        ]),
                    )
                    text = (resp.text or "").strip()
                    if len(text) >= 100:
                        # reset 429 count on success
                        _429_combo_count[(key_idx, model)] = 0
                        return text, f"{model} (key=***{key_suffix})"
                    # short/empty response — break retry loop, try next (key, model)
                    break
                except gerrors.ClientError as e:
                    err = str(e)
                    if "429" in err or "RESOURCE_EXHAUSTED" in err:
                        ckey = (key_idx, model)
                        _429_combo_count[ckey] = _429_combo_count.get(ckey, 0) + 1
                        if _429_combo_count[ckey] >= MAX_COMBO_429:
                            mark_cooldown(key_idx, model, key_suffix)
                            break  # try next key for same model
                        time.sleep(5)  # short backoff before next attempt on same key+model
                        continue
                    if "1048576" in err or "exceeds" in err.lower():
                        # long video — fall through to segmented path
                        log(f"  long video — segmenting {vid} via key=***{key_suffix} model={model}")
                        seg_result = try_segmented(client, model, url, key_suffix)
                        if seg_result:
                            _429_combo_count[(key_idx, model)] = 0
                            return seg_result, f"{model} segmented (key=***{key_suffix})"
                        break  # segmentation failed too — try next (key, model)
                    # other client error — non-recoverable on this combo
                    break
                except gerrors.ServerError:
                    if retry < 2:
                        time.sleep(20)
                        continue
                    break
                except Exception as e:
                    log(f"  unexpected on key=***{key_suffix} model={model}: {type(e).__name__}: {str(e)[:100]}")
                    break
    return None, None


def try_segmented(client, model: str, url: str, key_suffix: str) -> str | None:
    """Process video in 30-min segments up to 2h, merge results."""
    segments = []
    try:
        for seg_start in range(0, 7200, 1800):
            seg_end = seg_start + 1800
            try:
                seg_resp = client.models.generate_content(
                    model=model,
                    contents=gtypes.Content(parts=[
                        gtypes.Part(
                            file_data=gtypes.FileData(file_uri=url, mime_type="video/mp4"),
                            video_metadata=gtypes.VideoMetadata(
                                fps=FPS,
                                start_offset=f"{seg_start}s",
                                end_offset=f"{seg_end}s",
                            ),
                        ),
                        gtypes.Part(text=PROMPT),
                    ]),
                )
            except Exception as se:
                log(f"  segment err key=***{key_suffix}: {str(se)[:100]}")
                if not segments:
                    return None
                break
            seg_t = (seg_resp.text or "").strip()
            if seg_t and len(seg_t) >= 80:
                segments.append(f"### Segment {seg_start}s-{seg_end}s\n\n{seg_t}")
            elif not segments:
                return None
            else:
                break
        if segments:
            return "\n\n".join(segments)
    except Exception:
        return None
    return None


def load_queue():
    rows = []
    with QUEUE.open() as f:
        for line in f:
            parts = line.rstrip().split("\t")
            if len(parts) >= 3:
                rows.append(parts)
    return rows


def main():
    all_rows = load_queue()
    # First partition by HALF (account-level), then by CHUNK (job-level within account).
    # Row i belongs to this job iff it's in this account's half AND this chunk's slice.
    chunk_rows = [r for i, r in enumerate(all_rows)
                  if i % NUM_HALVES == HALF and (i // NUM_HALVES) % TOTAL == CHUNK]
    n_keys = len(ALL_KEYS)
    start_key_idx = CHUNK % n_keys
    log(f"start — total queue={len(all_rows)} my chunk={len(chunk_rows)} keys={n_keys} start_key_idx={start_key_idx}")

    ok = fail = 0
    started = time.time()
    quota_429_hits = 0
    # Cap runtime so the job EXITS and uploads its artifacts frequently (visible progress
    # every cycle) instead of running the full 350-min window. The queue is refreshed between
    # runs (harvest), so the next run resumes on the remaining vids — short chunks are resumable.
    MAX_RUNTIME_S = int(os.environ.get("MAX_RUNTIME_MIN", "70")) * 60

    for i, row in enumerate(chunk_rows, 1):
        if time.time() - started > MAX_RUNTIME_S:
            log(f"[{i}/{len(chunk_rows)}] RUNTIME-CAP hit ({MAX_RUNTIME_S//60}min) — exiting to upload artifacts (ok={ok})")
            break
        channel, url, vid = row[0], row[1], row[2]
        out_file = OUT_DIR / f"{vid}.md"
        if out_file.exists() and out_file.stat().st_size > 200:
            log(f"[{i}/{len(chunk_rows)}] SKIP {vid} (already done)")
            continue

        # short-circuit: if every (key, model) combo is cooling, wait until one expires
        if all_combos_cooling():
            wait_s = min_cooldown_wait()
            if wait_s > 0:
                log(f"[{i}/{len(chunk_rows)}] WAIT-COOLDOWN {vid} sleeping {wait_s:.0f}s (all combos cooling)")
                time.sleep(min(wait_s + 1, 120))  # cap at 2 min to keep moving

        t0 = time.time()
        # rotate starting key per video to spread load further within chunk
        rotate_offset = (start_key_idx + i) % n_keys
        result_text, used_model = try_video(url, vid, rotate_offset)
        dt = time.time() - t0

        if result_text:
            header = f"""---
chunk: {CHUNK}
channel: {channel}
video_id: {vid}
url: {url}
model: {used_model}
extracted_at: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}
---

# {vid}

## Gemini Multimodal Visual Analysis
_via {used_model} on GitHub Actions runner_

{result_text}
"""
            out_file.write_text(header)
            ok += 1
            if ok % 5 == 0:
                avg = (time.time() - started) / ok
                now = time.time()
                cooling_n = sum(1 for v in _cooldown_until.values() if v > now)
                log(f"[{i}/{len(chunk_rows)}] OK {used_model} {dt:.0f}s {vid} (ok={ok} fail={fail} avg={avg:.0f}s cooling={cooling_n}/{n_keys * len(MODELS)})")
        else:
            fail += 1
            log(f"[{i}/{len(chunk_rows)}] FAIL {vid}")

        time.sleep(2)

    now = time.time()
    cooling_n = sum(1 for v in _cooldown_until.values() if v > now)
    log(f"DONE chunk {CHUNK}: ok={ok} fail={fail} cooling={cooling_n}/{n_keys * len(MODELS)} elapsed={time.time()-started:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
