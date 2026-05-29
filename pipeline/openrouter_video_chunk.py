#!/usr/bin/env python3
"""
Pool 2 — OpenRouter free Gemini via YouTube video_url (SERVER-SIDE fetch, zero ban risk).

OpenRouter's /chat/completions accepts a `video_url` content part whose url is a YouTube link;
for Gemini-via-AI-Studio, OpenRouter passes the link to Google which fetches it server-side —
exactly like our direct-Gemini path, but drawing on OpenRouter's OWN independent free quota.
So this is a fully additive free pool with no local download and no YouTube ban exposure.

Verified: openrouter.ai/docs/guides/overview/multimodal/videos (YouTube links, server-side, Gemini/AI-Studio).

Env:
  OPENROUTER_KEYS_JSON  JSON array of OpenRouter API keys (rotated, per-key cooldown on 429)
  OPENROUTER_MODEL      model id (default a free Gemini variant; set to whatever is free when key exists)
  CHUNK_INDEX, TOTAL_CHUNKS, HALF, NUM_HALVES  same partition scheme as the Gemini chunk

Reverse-walks the queue (like the Groq pool) to minimize overlap with the front-walking Gemini halves.
Output schema identical to the Gemini chunk → same merge path.
"""
from __future__ import annotations
import os, sys, json, time, urllib.request, urllib.error
from pathlib import Path

CHUNK = int(os.environ["CHUNK_INDEX"])
TOTAL = int(os.environ["TOTAL_CHUNKS"])
HALF = int(os.environ.get("HALF", "0"))
NUM_HALVES = int(os.environ.get("NUM_HALVES", "1"))
KEYS = json.loads(os.environ["OPENROUTER_KEYS_JSON"])
MODEL = os.environ.get("OPENROUTER_MODEL", "google/gemini-2.0-flash-exp:free")
QUEUE = Path("queue/phase4-remaining.tsv")
OUT = Path(f"results/chunk-{CHUNK:02d}"); OUT.mkdir(parents=True, exist_ok=True)
LOG = OUT / "_chunk.log"
COOLDOWN_S = 65
MAX_TOKENS = 4000

PROMPT = """CRITICAL: The viewer ALREADY HAS THE FULL TRANSCRIPT. Do NOT transcribe or paraphrase spoken audio. Write ONLY about visible content the transcript cannot capture — every on-screen text, chart, slide, diagram, framework, brand/URL/logo, demo/screen-recording, and meaningful B-roll.

## Setting & production
## Timestamped visual events (EVERY visual change)  (MM:SS — what appears on screen)
## All visual frameworks  (every diagram/model/funnel/quadrant/flowchart — structure + labels)
## Brand & reference visual evidence  (every URL/handle/logo/product/software UI/book — exhaustive)
## Visual storytelling devices
## Speaker body-language peaks
If truly talking-head with zero meaningful visuals: one sentence saying so, then stop."""


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
                rows.append((p[0], p[1], p[2]))
    return rows


def call(key, url):
    body = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": PROMPT},
            {"type": "video_url", "video_url": {"url": url}},
        ]}],
        "max_tokens": MAX_TOKENS, "temperature": 0.2,
    }).encode()
    req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=body,
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            j = json.loads(r.read())
            return j["choices"][0]["message"]["content"], None
    except urllib.error.HTTPError as e:
        return None, ("429" if e.code == 429 else f"http{e.code}")
    except Exception as e:
        return None, str(e)[:80]


def main():
    rows = load_rows()[::-1]  # reverse-walk, opposite the Gemini front-halves
    mine = [r for i, r in enumerate(rows)
            if i % NUM_HALVES == HALF and (i // NUM_HALVES) % TOTAL == CHUNK]
    log(f"start — queue={len(rows)} my slice={len(mine)} keys={len(KEYS)} model={MODEL}")
    cooldown = {i: 0.0 for i in range(len(KEYS))}
    ki = CHUNK % len(KEYS)
    ok = fail = 0; t0 = time.time()
    for idx, (channel, url, vid) in enumerate(mine, 1):
        out = OUT / f"{vid}.md"
        if out.exists() and out.stat().st_size > 200:
            continue
        for _ in range(len(KEYS)):
            if time.time() >= cooldown[ki]:
                break
            ki = (ki + 1) % len(KEYS)
        else:
            time.sleep(min(max(0, min(cooldown.values()) - time.time()) + 1, COOLDOWN_S))
        text, err = call(KEYS[ki], url)
        if err == "429":
            cooldown[ki] = time.time() + COOLDOWN_S
            ki = (ki + 1) % len(KEYS)
            text, err = call(KEYS[ki], url)
        if not text or len(text) < 100:
            fail += 1; ki = (ki + 1) % len(KEYS); continue
        out.write_text(f"""---
chunk: {CHUNK}
channel: {channel}
video_id: {vid}
url: {url}
model: {MODEL} (openrouter video_url, server-side)
extracted_at: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}
---

# {vid}

## Gemini Multimodal Visual Analysis
_via {MODEL} (OpenRouter, server-side YouTube fetch)_

{text}
""")
        ok += 1; ki = (ki + 1) % len(KEYS)
        if ok % 5 == 0:
            log(f"[{idx}/{len(mine)}] OK {vid} (ok={ok} fail={fail} {ok/((time.time()-t0)/60):.1f}/min)")
    log(f"DONE ok={ok} fail={fail} elapsed={(time.time()-t0)/60:.1f}min")


if __name__ == "__main__":
    main()
