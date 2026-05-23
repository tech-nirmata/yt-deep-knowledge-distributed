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

PROMPT_TEMPLATE = """Extract EVERY piece of structured intelligence from this YouTube video transcript. Use ONLY information explicitly in the transcript. Capture EVERYTHING that matters — do not skip details to save space.

## URLs, handles, brands, products, people
EVERY URL, social handle (@username), brand name, product name, software tool, person's name, company explicitly mentioned. Include every mention even if duplicated across the transcript. One per line.

## ALL actionable takeaways
EVERY specific, concrete, actionable thing a viewer should do based on this video. Not just the top 5 — list ALL of them, regardless of count. Each as an imperative step with exact tactics, numbers, frameworks, or thresholds. Skip platitudes only.

## Frameworks, models, formulas, processes
EVERY named framework, mental model, formula, ratio, multi-step process, or system the speaker references. Name it + bullet list of the steps. Include even ones mentioned in passing.

## Quoted dollar figures, metrics, case studies, dates, statistics
EVERY specific number cited: dollar amounts, percentages, conversion rates, time periods, dates, ages, counts, ratios, case-study results. Include context for each. Do not filter; capture all.

## Key concepts, definitions, jargon
Any technical term, concept, or domain-specific language the speaker uses + how they define it (if they do).

## Quotes worth preserving
Any short memorable phrase, principle, or line that's quote-worthy.

## Core thesis (one sentence)
The single main claim or argument of this video, in ONE sentence.

## Secondary themes
Any other major topics, sub-arguments, or storylines woven through the transcript.

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

        # NO COMPROMISE: split very long transcripts into chunks instead of truncating.
        # llama-3.3-70b has 128K context (~96K tokens after prompt). Each char ~0.25 tokens.
        # Safe limit: 300K chars per call. Above that, multi-pass and merge.
        MAX_CHARS_PER_CALL = 300_000
        chunks = []
        if len(transcript) <= MAX_CHARS_PER_CALL:
            chunks = [transcript]
        else:
            # split into ~250K char chunks with 5K overlap to preserve context
            step = MAX_CHARS_PER_CALL - 5_000
            for start in range(0, len(transcript), step):
                chunks.append(transcript[start:start + MAX_CHARS_PER_CALL])

        all_enrichments = []
        chunk_failed = False
        for chunk_i, chunk_text in enumerate(chunks):
            prompt = PROMPT_TEMPLATE.format(transcript=chunk_text)
            if len(chunks) > 1:
                prompt = f"PART {chunk_i+1} of {len(chunks)} — combine with other parts later.\n\n" + prompt
            chunk_enrichment = None
            for retry in range(5):
                try:
                    resp = client.chat.completions.create(
                        model=model,
                        messages=[{"role":"user", "content": prompt}],
                        max_completion_tokens=4096,  # more headroom for thorough extraction
                        temperature=0.2,
                    )
                    chunk_enrichment = (resp.choices[0].message.content or "").strip()
                    if chunk_enrichment and len(chunk_enrichment) >= 100:
                        break
                    chunk_enrichment = None
                    break
                except RateLimitError:
                    wait = 20 + retry*15
                    time.sleep(wait)
                    continue
                except APIError as e:
                    err = str(e).lower()
                    if "context" in err or "token" in err:
                        # last-resort: smaller chunk
                        chunk_text = chunk_text[:int(len(chunk_text)*0.5)]
                        prompt = PROMPT_TEMPLATE.format(transcript=chunk_text)
                        if retry < 2:
                            continue
                    log(f"  APIErr {rel} chunk{chunk_i}: {str(e)[:120]}")
                    break
                except Exception as e:
                    log(f"  Err {rel} chunk{chunk_i}: {type(e).__name__}: {str(e)[:100]}")
                    break
            if chunk_enrichment:
                all_enrichments.append(chunk_enrichment)
            else:
                chunk_failed = True
        if chunk_failed and not all_enrichments:
            enrichment = None
        elif len(all_enrichments) > 1:
            enrichment = "\n\n---\n\n".join(
                f"### Part {i+1} of {len(all_enrichments)}\n\n{e}"
                for i, e in enumerate(all_enrichments)
            )
        else:
            enrichment = all_enrichments[0] if all_enrichments else None

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
