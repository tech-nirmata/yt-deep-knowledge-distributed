#!/usr/bin/env python3
"""
Phase 2 GROQ chunk processor — runs on GitHub Actions runner.
Reads phase2-input/**/*.md, processes slice by CHUNK_INDEX, outputs to phase2-output/<chunk>/.
"""
import os, sys, time, re
from pathlib import Path
from groq import Groq, RateLimitError, APIError

CHUNK = int(os.environ["CHUNK_INDEX"])
TOTAL = int(os.environ["TOTAL_CHUNKS"])
KEY = os.environ["GROQ_API_KEY"]
ROOT = Path("phase2-input")
OUT_DIR = Path(f"phase2-output/chunk-{CHUNK:02d}")
OUT_DIR.mkdir(parents=True, exist_ok=True)
LOG = OUT_DIR / "_chunk.log"

PROMPT_TEMPLATE = """Extract structured intelligence from this YouTube video transcript. Use ONLY information explicitly in the transcript.

## URLs, handles, brands, products, people
Every URL, social handle (@username), brand name, product name, software tool, person, or company explicitly mentioned. One per line.

## 5 actionable takeaways
Five specific, concrete actionable things a viewer should do. Imperative steps with exact tactics, numbers, frameworks, or thresholds.

## Frameworks, models, formulas
Any named framework, mental model, formula, ratio, multi-step process, or system. Name it + one-line summary. If none, write "None mentioned."

## Quoted dollar figures, metrics, case studies
Specific numbers cited. Include context.

## Core thesis (one sentence)
The single main claim or argument of this video, in ONE sentence.

---

TRANSCRIPT:
{transcript}
"""

ENRICH_MARKER = "## Enrichment (via Groq Llama)"

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

    client = Groq(api_key=KEY)
    ok = fail = 0
    started = time.time()
    model = "llama-3.3-70b-versatile"

    for i, fpath in enumerate(chunk_files, 1):
        rel = fpath.relative_to(ROOT)
        out_file = OUT_DIR / rel
        if out_file.exists() and out_file.stat().st_size > 500:
            continue

        try:
            text = fpath.read_text()
        except Exception:
            continue

        transcript = extract_transcript(text)
        if len(transcript) < 80:
            continue
        if len(transcript) > 80_000:
            transcript = transcript[:80_000] + "\n[truncated]"
        prompt = PROMPT_TEMPLATE.format(transcript=transcript)

        enrichment = None
        for retry in range(5):
            try:
                resp = client.chat.completions.create(
                    model=model,
                    messages=[{"role":"user", "content": prompt}],
                    max_completion_tokens=2048,
                    temperature=0.2,
                )
                enrichment = (resp.choices[0].message.content or "").strip()
                if enrichment and len(enrichment) >= 100:
                    break
                enrichment = None
                break
            except RateLimitError:
                wait = 20 + retry*15
                time.sleep(wait)
                continue
            except APIError as e:
                err = str(e).lower()
                if "context" in err or "token" in err:
                    transcript = transcript[:40_000] + "\n[heavily truncated]"
                    prompt = PROMPT_TEMPLATE.format(transcript=transcript)
                    if retry < 2:
                        continue
                log(f"  APIErr {rel}: {str(e)[:120]}")
                break
            except Exception as e:
                log(f"  Err: {type(e).__name__}: {str(e)[:100]}")
                break

        if enrichment:
            appendix = (
                f"\n\n---\n\n{ENRICH_MARKER}\n"
                f"_via {model} @ chunk {CHUNK} @ {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}_\n\n"
                f"{enrichment}\n"
            )
            out_file.parent.mkdir(parents=True, exist_ok=True)
            out_file.write_text(text.rstrip() + appendix)
            ok += 1
            if ok % 25 == 0:
                avg = (time.time() - started) / ok
                log(f"[{i}/{len(chunk_files)}] ok={ok} fail={fail} avg={avg:.1f}s")
        else:
            fail += 1

        time.sleep(1.5)

    log(f"DONE chunk {CHUNK}: ok={ok} fail={fail} elapsed={time.time()-started:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
