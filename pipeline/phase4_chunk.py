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
        # SPEED MODE: flash-lite-latest first (5-10x faster than pro, quality 3.00/3 per audit)
        # fps=0.5 = half the frames analyzed = 2x faster, still captures all visual events
        # If lite-latest fails, fall back to better models
        models = ["gemini-flash-lite-latest", "gemini-2.5-flash-lite", "gemini-flash-latest", "gemini-2.5-flash", "gemini-2.5-pro"]
        FPS = 0.5
        result_text = None
        used_model = None
        for model in models:
            for retry in range(3):
                try:
                    resp = client.models.generate_content(
                        model=model,
                        contents=gtypes.Content(parts=[
                            gtypes.Part(file_data=gtypes.FileData(file_uri=url, mime_type="video/mp4"),
                                       video_metadata=gtypes.VideoMetadata(fps=FPS)),
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
                    if "1048576" in err or "exceeds" in err.lower():
                        # too long — try segmented analysis: process video in 30-min chunks
                        # via startOffset/endOffset, then merge results
                        log(f"  long video — segmenting {vid}")
                        try:
                            segments = []
                            for seg_start in range(0, 7200, 1800):  # up to 2h, 30-min segments
                                seg_end = seg_start + 1800
                                seg_resp = client.models.generate_content(
                                    model=model,
                                    contents=gtypes.Content(parts=[
                                        gtypes.Part(file_data=gtypes.FileData(file_uri=url, mime_type="video/mp4"),
                                                   video_metadata=gtypes.VideoMetadata(
                                                       fps=FPS,
                                                       start_offset=f"{seg_start}s",
                                                       end_offset=f"{seg_end}s",
                                                   )),
                                        gtypes.Part(text=PROMPT),
                                    ]),
                                )
                                seg_t = (seg_resp.text or "").strip()
                                if seg_t and len(seg_t) >= 80:
                                    segments.append(f"### Segment {seg_start}s-{seg_end}s\n\n{seg_t}")
                                elif not segments:
                                    break  # first segment empty = video shorter than 30min, fallback won't help
                                else:
                                    break  # reached end of video
                            if segments:
                                result_text = "\n\n".join(segments)
                                used_model = model + f" (segmented {len(segments)} parts)"
                                break
                        except Exception as e2:
                            log(f"  segment err: {str(e2)[:100]}")
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
