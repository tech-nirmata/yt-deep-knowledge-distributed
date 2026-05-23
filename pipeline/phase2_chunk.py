#!/usr/bin/env python3
"""
Phase 2 chunk processor — runs on a GitHub Actions runner with one Gemini key.
Reads phase2-input/**/*.md, processes its slice by CHUNK_INDEX, outputs
enriched files to phase2-output/<chunk>/.
"""
import os, sys, time, json, re
from pathlib import Path
from google import genai
from google.genai import errors as gerrors

CHUNK = int(os.environ["CHUNK_INDEX"])
TOTAL = int(os.environ["TOTAL_CHUNKS"])
KEY = os.environ["GEMINI_API_KEY"]
ROOT = Path("phase2-input")
OUT_DIR = Path(f"phase2-output/chunk-{CHUNK:02d}")
OUT_DIR.mkdir(parents=True, exist_ok=True)
LOG = OUT_DIR / "_chunk.log"

PROMPT_TEMPLATE = """Extract structured intelligence from this YouTube video transcript. Use ONLY information in the transcript. Be concrete and specific.

## URLs, handles, brands, products, people
Every URL, social handle (@username), brand name, product name, software tool, person, or company explicitly mentioned. One per line.

## 5 actionable takeaways
Five specific, concrete actionable things a viewer should do. Imperative steps with exact tactics, numbers, frameworks, or thresholds. Skip platitudes.

## Frameworks, models, formulas
Any named framework, mental model, formula, ratio, multi-step process, or system the speaker references. Name it + one-line summary of steps. If none, write "None mentioned."

## Quoted dollar figures, metrics, case studies
Specific numbers cited: dollar amounts, percentages, conversion rates, time periods, case-study results. Include context. Skip if none.

## Core thesis (one sentence)
The single main claim or argument of this video, in ONE sentence.

---

TRANSCRIPT:
{transcript}
"""

def log(msg):
    line = f"[{time.strftime('%H:%M:%S')} c{CHUNK}] {msg}"
    print(line, flush=True)
    with LOG.open("a") as f: f.write(line + "\n")


def extract_transcript(text):
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end >= 0:
            text = text[end+5:]
    parts = text.split("\n\n---\n\n")
    return parts[0].strip()


def main():
    all_files = sorted(ROOT.rglob("*.md"))
    chunk_files = [f for i, f in enumerate(all_files) if i % TOTAL == CHUNK]
    log(f"start — total={len(all_files)} my chunk={len(chunk_files)} key=***{KEY[-6:]}")

    client = genai.Client(api_key=KEY)
    ok = fail = 0
    started = time.time()

    models = ["gemini-2.5-flash", "gemini-flash-latest", "gemini-2.5-flash-lite", "gemini-flash-lite-latest"]

    for i, fpath in enumerate(chunk_files, 1):
        # output path — preserve notebook_id structure under chunk dir
        rel = fpath.relative_to(ROOT)
        out_file = OUT_DIR / rel
        if out_file.exists() and out_file.stat().st_size > 200:
            continue

        try:
            text = fpath.read_text()
            transcript = extract_transcript(text)
            if len(transcript) < 80:
                continue
            if len(transcript) > 100_000:
                transcript = transcript[:100_000] + "\n[transcript truncated]"
            prompt = PROMPT_TEMPLATE.format(transcript=transcript)
        except Exception as e:
            log(f"  read err: {e}")
            fail += 1
            continue

        enrichment = None
        used_model = None
        for model in models:
            for retry in range(3):
                try:
                    resp = client.models.generate_content(model=model, contents=prompt)
                    t = (resp.text or "").strip()
                    if len(t) >= 100:
                        enrichment = t
                        used_model = model
                        break
                    break
                except gerrors.ClientError as e:
                    err = str(e)
                    if "429" in err or "RESOURCE_EXHAUSTED" in err:
                        if retry < 2:
                            time.sleep(30 + retry * 30)
                            continue
                        break
                    break
                except gerrors.ServerError:
                    if retry < 2:
                        time.sleep(20)
                        continue
                    break
                except Exception:
                    break
            if enrichment:
                break

        if enrichment:
            appendix = (
                f"\n\n---\n\n## Enrichment (via Gemini text)\n"
                f"_via {used_model} @ chunk {CHUNK} @ {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}_\n\n"
                f"{enrichment}\n"
            )
            out_file.parent.mkdir(parents=True, exist_ok=True)
            out_file.write_text(text.rstrip() + appendix)
            ok += 1
            if ok % 25 == 0:
                avg = (time.time() - started) / ok
                log(f"[{i}/{len(chunk_files)}] OK {used_model} ok={ok} fail={fail} avg={avg:.1f}s")
        else:
            fail += 1

        time.sleep(1.5)

    log(f"DONE chunk {CHUNK}: ok={ok} fail={fail} elapsed={time.time()-started:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
