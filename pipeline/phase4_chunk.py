#!/usr/bin/env python3
"""
Phase 4 chunk processor — runs on a single GitHub Actions runner.
Reads queue/phase4-remaining.tsv, processes its slice based on CHUNK_INDEX
and TOTAL_CHUNKS env vars, outputs results to results/<chunk>/.
"""
import os, sys, time, json, signal, hashlib
from pathlib import Path
from google import genai
from google.genai import types as gtypes, errors as gerrors

CHUNK = int(os.environ["CHUNK_INDEX"])
TOTAL = int(os.environ["TOTAL_CHUNKS"])
KEY = os.environ["GEMINI_API_KEY"]
QUEUE = Path("queue/phase4-remaining.tsv")
OUT_DIR = Path(f"results/chunk-{CHUNK:02d}")
OUT_DIR.mkdir(parents=True, exist_ok=True)
LOG = OUT_DIR / "_chunk.log"

PROMPT = """CRITICAL: The viewer ALREADY HAS THE FULL TRANSCRIPT. Do NOT transcribe, paraphrase, or quote anything the speaker says. Write ONLY about visible content the transcript cannot capture.

Required output (markdown sections):

## Setting & production
Location, camera angle, wardrobe, props, lighting, background.

## Timestamped visual events
ONLY non-audio content. Each entry: `MM:SS — what appears on screen`. On-screen text, slides, charts, screen recordings, B-roll, whiteboard, demos, dashboards, screenshots.

## Visual frameworks
Diagrams/models/frameworks shown — describe structure so someone could redraw.

## Brand & reference visual evidence
URLs, social handles, brand logos, product names visually present.

## Visual storytelling devices
Pattern interrupts, zoom-ins, cuts, transitions that change meaning.

If talking-head only with no visuals: one sentence stating so."""

def log(msg):
    line = f"[{time.strftime('%H:%M:%S')} c{CHUNK}] {msg}"
    print(line, flush=True)
    with LOG.open("a") as f: f.write(line + "\n")

def load_queue():
    rows = []
    with QUEUE.open() as f:
        for line in f:
            parts = line.rstrip().split("\t")
            if len(parts) >= 3:
                rows.append(parts)  # [channel, url, vid, priority?]
    return rows

def main():
    all_rows = load_queue()
    # split into TOTAL chunks, take chunk CHUNK
    chunk_rows = [r for i, r in enumerate(all_rows) if i % TOTAL == CHUNK]
    log(f"start — total queue={len(all_rows)} my chunk={len(chunk_rows)} key=***{KEY[-6:]}")

    client = genai.Client(api_key=KEY)
    ok = fail = 0
    started = time.time()
    quota_429_hits = 0

    for i, row in enumerate(chunk_rows, 1):
        channel, url, vid = row[0], row[1], row[2]
        out_file = OUT_DIR / f"{vid}.md"
        if out_file.exists() and out_file.stat().st_size > 200:
            log(f"[{i}/{len(chunk_rows)}] SKIP {vid} (already done)")
            continue

        t0 = time.time()
        # try a few models in order
        models = ["gemini-2.5-flash", "gemini-flash-latest", "gemini-2.5-flash-lite", "gemini-flash-lite-latest"]
        result_text = None
        used_model = None
        for model in models:
            for retry in range(3):
                try:
                    resp = client.models.generate_content(
                        model=model,
                        contents=gtypes.Content(parts=[
                            gtypes.Part(file_data=gtypes.FileData(file_uri=url, mime_type="video/mp4"),
                                       video_metadata=gtypes.VideoMetadata(fps=0.5)),
                            gtypes.Part(text=PROMPT),
                        ]),
                    )
                    t = (resp.text or "").strip()
                    if len(t) >= 100:
                        result_text = t
                        used_model = model
                        break
                    break
                except gerrors.ClientError as e:
                    err = str(e)
                    if "429" in err or "RESOURCE_EXHAUSTED" in err:
                        quota_429_hits += 1
                        if retry < 2:
                            time.sleep(45 + retry * 30)
                            continue
                        break
                    if "1048576" in err:
                        # too long — retry with fps=0.2
                        try:
                            resp = client.models.generate_content(
                                model=model,
                                contents=gtypes.Content(parts=[
                                    gtypes.Part(file_data=gtypes.FileData(file_uri=url, mime_type="video/mp4"),
                                               video_metadata=gtypes.VideoMetadata(fps=0.2)),
                                    gtypes.Part(text=PROMPT),
                                ]),
                            )
                            t = (resp.text or "").strip()
                            if len(t) >= 100:
                                result_text = t
                                used_model = model + " (fps=0.2)"
                                break
                        except Exception:
                            pass
                    break
                except gerrors.ServerError as e:
                    if retry < 2:
                        time.sleep(20)
                        continue
                    break
                except Exception as e:
                    log(f"  unexpected: {type(e).__name__}: {str(e)[:120]}")
                    break
            if result_text:
                break

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
                log(f"[{i}/{len(chunk_rows)}] OK {used_model} {dt:.0f}s {vid} (ok={ok} fail={fail} avg={avg:.0f}s 429s={quota_429_hits})")
        else:
            fail += 1
            log(f"[{i}/{len(chunk_rows)}] FAIL {vid}")

        # gentle pacing — GitHub IP is fresh, less throttled, but be polite
        time.sleep(2)

    log(f"DONE chunk {CHUNK}: ok={ok} fail={fail} elapsed={time.time()-started:.0f}s")
    return 0

if __name__ == "__main__":
    sys.exit(main())
