#!/usr/bin/env python3
"""
Groq cloud chunk — runs ON a GitHub Actions runner (Azure IP, disposable).

INDEPENDENT free pool, separate daily quota from Gemini:
  - yt-dlp downloads the video on the RUNNER (never our home IP → no ban risk to Parth)
  - ffmpeg extracts 5 keyframes
  - Groq Llama-4-Scout vision analyzes the frames (Groq's free 1000 RPD/key, 4 keys)
  - output → results/chunk-NN/<vid>.md  (same schema as Gemini chunks → same merge path)

Anti-overlap with Gemini A/B: this worker walks its slice in REVERSE queue order,
so it chews from the BACK while Gemini chews the front (even/odd halves). They only
overlap where they converge in the middle; the local merge dedupes by vid anyway.

Env: CHUNK_INDEX, TOTAL_CHUNKS, GROQ_KEYS_JSON
"""
from __future__ import annotations
import os, sys, json, time, base64, subprocess
from pathlib import Path
import urllib.request

CHUNK = int(os.environ["CHUNK_INDEX"])
TOTAL = int(os.environ["TOTAL_CHUNKS"])
KEYS = json.loads(os.environ["GROQ_KEYS_JSON"])
QUEUE = Path("queue/phase4-remaining.tsv")
OUT = Path(f"results/chunk-{CHUNK:02d}"); OUT.mkdir(parents=True, exist_ok=True)
LOG = OUT / "_chunk.log"

MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"
N_FRAMES = 5            # Scout caps at 5 images/call
MAX_TOKENS = 4000
COOLDOWN_S = 75         # per-key cooldown after 429 (Groq RPM heals fast)

PROMPT = """You are analyzing 5 keyframes from a YouTube video, in chronological order. The viewer ALREADY has the audio transcript — describe ONLY visual content the transcript can't capture.

## Setting & production
Location, camera, wardrobe, props, lighting, background; note changes across frames.

## Timestamped visual events (EVERY visual change)
For each frame (Frame 1..5, mapped roughly to video time): on-screen text/graphics/charts/slide content (verbatim), brands/URLs/logos visible, demos or screen recordings, B-roll. Be exhaustive.

## All visual frameworks
EVERY diagram, model, matrix, funnel, quadrant, flowchart, pendulum shown — structure + labels in enough detail to reconstruct.

## Brand & reference visual evidence
EVERY URL, social handle, brand logo, product name, software UI, book cover. List exhaustively.

## Visual storytelling devices
Pattern interrupts, zoom-ins, color shifts, lower-thirds — only when they change meaning.

If the 5 frames are near-identical talking-head with no meaningful visuals: write one sentence saying so and stop."""


def log(m):
    line = f"[{time.strftime('%H:%M:%S')} c{CHUNK}] {m}"
    print(line, flush=True)
    with LOG.open("a") as f:
        f.write(line + "\n")


def load_rows():
    rows = []
    with QUEUE.open() as f:
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) >= 3:
                rows.append((p[0], p[1], p[2]))  # channel, url, vid
    return rows


def extract_frames(vid: str, url: str) -> list[Path]:
    d = Path(f"/tmp/fr/{vid}"); d.mkdir(parents=True, exist_ok=True)
    src = d / "s.mp4"
    try:
        subprocess.run(
            ["yt-dlp", "-f", "best[height<=480][ext=mp4]/best[height<=720][ext=mp4]/worst[ext=mp4]",
             "--no-warnings", "--quiet", "--ignore-errors", "--no-playlist",
             "--max-filesize", "600M", "--socket-timeout", "45", "--retries", "2",
             "-o", str(src), url],
            capture_output=True, timeout=300)
    except Exception:
        return []
    if not src.exists() or src.stat().st_size == 0:
        return []
    # duration
    try:
        dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                              "-of", "csv=p=0", str(src)], capture_output=True, text=True, timeout=30).stdout.strip().split(".")[0]
        dur = int(dur) if dur.isdigit() else 300
    except Exception:
        dur = 300
    if dur < 1:
        dur = 300
    subprocess.run(["ffmpeg", "-y", "-i", str(src), "-vf", f"fps={N_FRAMES}/{dur},scale=1280:-2",
                    "-frames:v", str(N_FRAMES), "-q:v", "2", str(d / "f_%02d.jpg")],
                   capture_output=True, timeout=120)
    src.unlink(missing_ok=True)
    return sorted(d.glob("f_*.jpg"))[:N_FRAMES]


def cleanup(vid: str):
    d = Path(f"/tmp/fr/{vid}")
    if d.exists():
        for f in d.iterdir():
            f.unlink(missing_ok=True)
        d.rmdir()


def groq_call(key: str, frames: list[Path]):
    content = [{"type": "text", "text": PROMPT}]
    for f in frames:
        b64 = base64.b64encode(f.read_bytes()).decode()
        content.append({"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}})
    body = json.dumps({"model": MODEL, "messages": [{"role": "user", "content": content}],
                       "max_tokens": MAX_TOKENS, "temperature": 0.2}).encode()
    req = urllib.request.Request("https://api.groq.com/openai/v1/chat/completions", data=body,
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            j = json.loads(r.read())
            return j["choices"][0]["message"]["content"], None
    except urllib.error.HTTPError as e:
        return None, ("429" if e.code == 429 else f"http{e.code}")
    except Exception as e:
        return None, str(e)[:80]


def main():
    rows = load_rows()
    # reverse-order slice: walk from the back, opposite the Gemini front-halves
    rows = rows[::-1]
    mine = [r for i, r in enumerate(rows) if i % TOTAL == CHUNK]
    log(f"start — queue={len(rows)} my slice={len(mine)} keys={len(KEYS)} (reverse walk)")

    cooldown = {i: 0.0 for i in range(len(KEYS))}
    ok = fail = exf = 0
    ki = CHUNK % len(KEYS)
    t0 = time.time()

    for idx, (channel, url, vid) in enumerate(mine, 1):
        out = OUT / f"{vid}.md"
        if out.exists() and out.stat().st_size > 200:
            continue
        frames = extract_frames(vid, url)
        if len(frames) < 3:
            exf += 1; cleanup(vid)
            if exf <= 3 or exf % 25 == 0:
                log(f"[{idx}/{len(mine)}] EXTRACT-FAIL {vid} (count={exf})")
            continue
        # pick a non-cooling key
        text = None
        for _ in range(len(KEYS)):
            if time.time() >= cooldown[ki]:
                break
            ki = (ki + 1) % len(KEYS)
        else:
            wait = max(0, min(cooldown.values()) - time.time())
            time.sleep(min(wait + 1, COOLDOWN_S))
        key = KEYS[ki]
        text, err = groq_call(key, frames)
        cleanup(vid)
        if err == "429":
            cooldown[ki] = time.time() + COOLDOWN_S
            ki = (ki + 1) % len(KEYS)
            # one retry on the next key
            key = KEYS[ki]
            text, err = groq_call(key, frames)
        if not text or len(text) < 100:
            fail += 1
            ki = (ki + 1) % len(KEYS)
            continue
        out.write_text(f"""---
chunk: {CHUNK}
channel: {channel}
video_id: {vid}
url: {url}
model: {MODEL} ({N_FRAMES} frames, groq, GHA runner)
extracted_at: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}
---

# {vid}

## Gemini Multimodal Visual Analysis
_via {MODEL} (groq, {N_FRAMES} frames) on GitHub Actions runner_

{text}
""")
        ok += 1
        ki = (ki + 1) % len(KEYS)
        if ok % 5 == 0:
            el = time.time() - t0
            log(f"[{idx}/{len(mine)}] OK {vid} (ok={ok} fail={fail} exf={exf} {ok/(el/60):.1f}/min)")

    log(f"DONE ok={ok} fail={fail} extract_fail={exf} elapsed={(time.time()-t0)/60:.1f}min")


if __name__ == "__main__":
    main()
