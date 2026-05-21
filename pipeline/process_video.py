#!/usr/bin/env python3
"""v4 — MAX SPEED + MAX QUALITY free pipeline.

Upgrades over v3:
  - Multi-provider vision pool (Gemini × 4 + Groq + Cerebras + local fallbacks)
  - Concurrent frame-batch dispatch within each video (parallel batches to different providers)
  - Parallel pre-fetch of metadata, captions, comments
  - whisper.cpp Metal for ASR (same as v3)
  - All scraping async
  - Output: rich markdown + structured for LLM retrieval
"""
import argparse, asyncio, base64, json, os, re, shutil, subprocess, sys, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

OUTPUT_ROOT = Path(os.environ.get("OUTPUT_ROOT") or "docs")
TMP_ROOT = Path("/tmp/yt-deep-knowledge")
TMP_ROOT.mkdir(parents=True, exist_ok=True)

WHISPER_BIN = os.environ.get("WHISPER_BIN") or ("/opt/homebrew/bin/whisper-cli" if os.path.exists("/opt/homebrew/bin/whisper-cli") else "/usr/local/bin/whisper-cli")
WHISPER_MODEL = os.path.expanduser("~/.whisper-models/ggml-base.en.bin")
RESOLUTION = 768            # OCR-grade — small on-screen text (URLs, slide bullets, code) stays readable
MAX_FRAMES = 200            # hard cap (was 30) — 1 frame per ~15-30s for typical content
MIN_SECS_PER_FRAME = 12     # adaptive: longer videos get more frames, short videos fewer
BATCH_SIZE = 5              # Groq Llama-4-Scout cap; Gemini chunks within batch
SCRAPE_TIMEOUT = 25         # was 8 — let slow legit pages finish
SCRAPE_DEPTH = 2            # follow links from scraped pages 1 more level
SCRAPE_RETRIES = 1
MAX_COMMENTS = 500          # was 100; cap to bound doc size on viral videos
RAW_FRAMES_DIR = Path(os.environ.get("RAW_FRAMES_DIR") or "_raw_frames")
RAW_FRAMES_DIR.mkdir(parents=True, exist_ok=True)

# Import vision pool
sys.path.insert(0, str(Path(__file__).parent))
from vision_pool import get_pool



def _yt_cookie_args():
    """Return cookie flags based on env. Local mac uses Chrome; runner uses cookies.txt if provided."""
    if os.environ.get("YT_DLP_COOKIES_BROWSER"):
        return ["--cookies-from-browser", os.environ["YT_DLP_COOKIES_BROWSER"]]
    if os.environ.get("YT_DLP_COOKIES_FILE") and os.path.exists(os.environ["YT_DLP_COOKIES_FILE"]):
        return ["--cookies", os.environ["YT_DLP_COOKIES_FILE"]]
    return []

def log(msg, tag=""):
    ts = time.strftime("%H:%M:%S")
    print(f"[{ts}]{'['+tag+']' if tag else ''} {msg}", flush=True)


def run(cmd, timeout=900):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def video_id_from_url(url):
    m = re.search(r"(?:v=|/shorts/|youtu\.be/)([A-Za-z0-9_-]{11})", url)
    return m.group(1) if m else None


# ---------- yt-dlp ----------

def yt_metadata(url, with_comments=True):
    args = ["yt-dlp", *_yt_cookie_args(), "--skip-download",
            "--write-auto-subs", "--sub-lang", "en", "--sub-format", "vtt",
            "-o", str(TMP_ROOT / "%(id)s.%(ext)s"),
            "--dump-json", "--no-warnings"]
    if with_comments:
        args += ["--write-comments",
                 "--extractor-args",
                 f"youtube:comment_sort=top;max_comments={MAX_COMMENTS},all,{MAX_COMMENTS}"]
    args.append(url)
    r = run(args, timeout=180)
    if not r.stdout.strip():
        raise RuntimeError(f"yt-dlp empty: {r.stderr[-300:]}")
    meta = json.loads(r.stdout)
    transcript = None
    vtt = TMP_ROOT / f"{meta['id']}.en.vtt"
    if vtt.exists():
        transcript = vtt_to_text(vtt.read_text())
    return meta, transcript, meta.get("comments") or []


def vtt_to_text(vtt):
    segments, cur = [], None
    for line in vtt.splitlines():
        line = line.strip()
        if "-->" in line:
            if cur: segments.append(cur)
            a, b = line.split(" --> ")[0:2]
            cur = {"start": a.split(".")[0], "end": b.split(" ")[0].split(".")[0], "text": ""}
        elif line and not line.startswith(("WEBVTT","Kind:","Language:","NOTE")) and cur is not None:
            clean = re.sub(r"<[^>]+>", "", line)
            if clean:
                cur["text"] = (cur["text"] + " " + clean).strip()
    if cur: segments.append(cur)
    out, last = [], None
    for s in segments:
        if s["text"] and s["text"] != last:
            out.append(s); last = s["text"]
    return out


def download_video(url, vid_id):
    out = TMP_ROOT / f"{vid_id}.mp4"
    if out.exists():
        return out
    run(["yt-dlp", *_yt_cookie_args(),
         "-f", "best[height<=480]/best", "-o", str(out),
         "--no-warnings", "--quiet", url], timeout=600)
    if out.exists():
        return out
    for ext in ("webm", "mkv"):
        p = TMP_ROOT / f"{vid_id}.{ext}"
        if p.exists(): return p
    raise RuntimeError("download failed")


# ---------- whisper.cpp ----------

def whisper_cpp_transcribe(video_path):
    """Local fallback (whisper.cpp Metal)."""
    wav = video_path.with_suffix(".wav")
    run(["ffmpeg", "-y", "-i", str(video_path), "-ar", "16000", "-ac", "1",
         "-c:a", "pcm_s16le", str(wav)], timeout=300)
    out_base = video_path.with_suffix("")
    run([WHISPER_BIN, "-m", WHISPER_MODEL, "-f", str(wav),
         "-t", "8", "-of", str(out_base), "-ojf", "--no-prints"], timeout=900)
    json_out = out_base.with_suffix(".json")
    segments = []
    if json_out.exists():
        data = json.loads(json_out.read_text())
        for s in data.get("transcription", []):
            t0 = s["timestamps"]["from"]
            t1 = s["timestamps"]["to"]
            segments.append({
                "start": t0.split(",")[0],
                "end": t1.split(",")[0],
                "text": s["text"].strip(),
            })
        json_out.unlink()
    wav.unlink(missing_ok=True)
    return segments, "whisper_cpp_metal_local"


def whisper_groq_transcribe(video_path):
    """Groq whisper-large-v3-turbo via 16kbps mono MP3 (handles up to ~3.5h audio in 25MB)."""
    if not os.environ.get("GROQ_API_KEY"):
        env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
        if os.path.exists(env_path):
            for line in open(env_path):
                if "=" in line:
                    k, v = line.strip().split("=", 1)
                    if k not in os.environ:
                        os.environ[k] = v
    from groq import Groq
    mp3 = video_path.with_suffix(".mp3")
    # 16kbps mono MP3 → ~120 KB/min. 25 MB ≈ 3.5h. Sufficient for any YouTube video.
    run(["ffmpeg", "-y", "-i", str(video_path), "-ar", "16000", "-ac", "1",
         "-b:a", "16k", "-f", "mp3", str(mp3)], timeout=300)
    file_size_mb = os.path.getsize(mp3) / 1024 / 1024
    if file_size_mb > 24:
        mp3.unlink(missing_ok=True)
        raise RuntimeError(f"audio still too large after mp3 compression ({file_size_mb:.1f}MB)")
    client = Groq()
    with open(mp3, "rb") as f:
        r = client.audio.transcriptions.create(
            file=(mp3.name, f.read()),
            model="whisper-large-v3-turbo",
            response_format="verbose_json",
        )
    segs = []
    for s in r.segments:
        st = s.get("start", 0) if isinstance(s, dict) else s.start
        en = s.get("end", 0) if isinstance(s, dict) else s.end
        tx = s.get("text", "") if isinstance(s, dict) else s.text
        segs.append({
            "start": f"{int(st//60):02d}:{int(st%60):02d}",
            "end": f"{int(en//60):02d}:{int(en%60):02d}",
            "text": tx.strip(),
        })
    mp3.unlink(missing_ok=True)
    return segs, "groq_whisper_large_v3_turbo"


def transcribe(video_path):
    """Groq primary, whisper.cpp Metal fallback."""
    try:
        segs, src = whisper_groq_transcribe(video_path)
        if segs:
            return segs, src
    except Exception as e:
        log(f"groq whisper failed ({type(e).__name__}); falling back to local: {str(e)[:120]}", "whisper")
    return whisper_cpp_transcribe(video_path)


# ---------- frames ----------

def extract_frames(video_path):
    frames_dir = TMP_ROOT / f"{video_path.stem}_frames"
    if frames_dir.exists():
        shutil.rmtree(frames_dir)
    frames_dir.mkdir()
    scenes_dir = frames_dir / "scenes"; scenes_dir.mkdir()
    run(["ffmpeg", "-y", "-hwaccel", "videotoolbox", "-i", str(video_path),
         "-vf", f"select='gt(scene\\,0.30)',scale={RESOLUTION}:-1",
         "-vsync", "vfr", "-q:v", "5",
         str(scenes_dir / "scene_%05d.jpg")], timeout=600)
    base_dir = frames_dir / "base"; base_dir.mkdir()
    run(["ffmpeg", "-y", "-hwaccel", "videotoolbox", "-i", str(video_path),
         "-vf", f"fps=0.33,scale={RESOLUTION}:-1", "-q:v", "5",
         str(base_dir / "base_%05d.jpg")], timeout=600)
    return sorted(scenes_dir.glob("*.jpg")), sorted(base_dir.glob("*.jpg")), frames_dir


def dedupe_frames(scene_frames, base_frames, duration_sec=0, hamming=6):
    """Adaptive frame cap: at least 1 frame per MIN_SECS_PER_FRAME of video.
    Tighter perceptual hash threshold (was 8, now 6) keeps more distinct frames.
    Scene frames prioritized over uniform base frames."""
    import imagehash
    from PIL import Image
    # Adaptive cap: longer videos → more frames; bounded by MAX_FRAMES
    adaptive_cap = max(30, min(MAX_FRAMES, int(duration_sec / MIN_SECS_PER_FRAME))) if duration_sec else MAX_FRAMES
    ordered = list(scene_frames) + list(base_frames)
    seen, kept = [], []
    for p in ordered:
        if len(kept) >= adaptive_cap: break
        try:
            h = imagehash.phash(Image.open(p))
        except Exception:
            continue
        if any((h - sh) <= hamming for sh in seen[-30:]):
            continue
        kept.append(p); seen.append(h)
    return kept, adaptive_cap


def save_raw_frames(unique_frames, vid_id):
    """Persist deduped raw frames so we can re-analyze with stronger models later."""
    out_dir = RAW_FRAMES_DIR / vid_id
    out_dir.mkdir(parents=True, exist_ok=True)
    for i, src in enumerate(unique_frames):
        dst = out_dir / f"frame_{i:04d}.jpg"
        if not dst.exists():
            try:
                shutil.copy(src, dst)
            except Exception:
                pass
    return out_dir


# ---------- concurrent vision via pool ----------

def describe_frames_concurrent(frame_paths, duration):
    """Dispatch frame batches to vision providers IN PARALLEL.
    Each batch goes to a different provider when possible (round-robin in pool).
    Returns ordered list of {timestamp, description}."""
    pool = get_pool()
    n = len(frame_paths)
    # Split into batches
    batches = [frame_paths[i:i+BATCH_SIZE] for i in range(0, n, BATCH_SIZE)]
    log(f"vision: dispatching {len(batches)} concurrent batches of <={BATCH_SIZE} frames", "vision")
    results_per_batch = [None] * len(batches)
    t0 = time.time()

    def do_batch(bi):
        try:
            descs, provider, elapsed = pool.describe_batch(batches[bi])
            return bi, descs, provider, elapsed, None
        except Exception as e:
            return bi, None, None, 0, e

    # Concurrent dispatch — workers=len(batches) but pool's internal cooldown handles cycling
    with ThreadPoolExecutor(max_workers=min(len(batches), 8)) as ex:
        futs = [ex.submit(do_batch, bi) for bi in range(len(batches))]
        for fut in as_completed(futs):
            bi, descs, provider, elapsed, err = fut.result()
            if err:
                log(f"  batch {bi}: FAIL {err}", "vision")
                results_per_batch[bi] = ["[failed]"] * len(batches[bi])
            else:
                log(f"  batch {bi}: {provider} in {elapsed:.1f}s ({len(descs)} descs)", "vision")
                results_per_batch[bi] = descs

    # Flatten ordered
    flat_descs = [d for batch_descs in results_per_batch for d in batch_descs]
    # Attach timestamps
    out = []
    for i, d in enumerate(flat_descs):
        ts_sec = (i / max(n-1, 1)) * duration if duration else 0
        ts = f"{int(ts_sec//60):02d}:{int(ts_sec%60):02d}"
        out.append({"timestamp": ts, "description": d})
    log(f"vision done in {time.time()-t0:.1f}s for {n} frames", "vision")
    return out


# ---------- async scraping ----------

def extract_urls(text):
    """Aggressive URL extraction — full URLs + naked domains + common patterns."""
    if not text: return []
    urls = set()
    # 1. Full URLs
    urls.update(re.findall(r"https?://[^\s<>\"\)\]\}]+", text))
    # 2. Naked domains commonly mentioned in videos (notion.so/xyz, opbot.io, etc)
    naked = re.findall(
        r"\b(?:(?:notion\.so|notion\.com|opbot\.io|skool\.com|gumroad\.com|"
        r"airtable\.com|typeform\.com|calendly\.com|google\.com|drive\.google\.com|"
        r"docs\.google\.com|github\.com|gitlab\.com|linkedin\.com|twitter\.com|"
        r"x\.com|instagram\.com|tiktok\.com|t\.me|loom\.com|substack\.com|"
        r"beehiiv\.com|convertkit\.com|mailchimp\.com|hubspot\.com|stripe\.com|"
        r"shopify\.com|webflow\.com|framer\.com|figma\.com|miro\.com|"
        r"discord\.gg|discord\.com|patreon\.com|youtu\.be|"
        r"[a-zA-Z0-9-]+\.(?:com|io|ai|app|co|dev|net|org|so|me))"
        r"/[A-Za-z0-9_\-\./?&=%~+#]+)\b", text, re.IGNORECASE
    )
    for u in naked:
        urls.add("https://" + u)
    # Strip trailing punctuation
    cleaned = set()
    for u in urls:
        u = u.rstrip(".,;:!?")
        if len(u) > 10:
            cleaned.add(u)
    return list(cleaned)


def extract_urls_from_all(meta, transcript, frame_descs):
    """Union URLs from description + transcript text + vision frame descriptions."""
    all_text = []
    all_text.append(meta.get("description","") or "")
    for seg in transcript or []:
        all_text.append(seg.get("text",""))
    for fd in frame_descs or []:
        all_text.append(fd.get("description",""))
    combined = "\n".join(all_text)
    return extract_urls(combined)


SKIP_DOMAINS = (
    "googletagmanager", "google-analytics", "doubleclick", "googleads",
    "facebook.com/tr", "fb.com/tr", "instagram.com/embed",
    "fonts.googleapis", "fonts.gstatic", "cdnjs", "cdn.jsdelivr",
)


async def fetch(session, url, max_chars=12000, attempt=0):
    """Scrape one URL with retry + 25s timeout. Returns html metadata + child links for recursion."""
    if any(s in url.lower() for s in SKIP_DOMAINS):
        return {"url": url, "kind": "skip", "note": "tracker/CDN"}
    try:
        async with session.get(url, timeout=SCRAPE_TIMEOUT, allow_redirects=True,
                                headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}) as r:
            r.raise_for_status()
            final_url = str(r.url)
            if "youtube.com" in final_url or "youtu.be" in final_url:
                return {"url": url, "final": final_url, "kind": "youtube",
                        "note": "skipped (would recurse into video)", "child_urls": []}
            ct = r.headers.get("Content-Type","")
            if "text/html" not in ct and "text/plain" not in ct:
                return {"url": url, "final": final_url, "kind": ct.split(";")[0],
                        "note": "non-HTML", "child_urls": []}
            text = await r.text()
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(text, "lxml")
            for t in soup(["script","style","noscript"]): t.decompose()
            title = soup.title.string.strip() if soup.title and soup.title.string else ""
            body = re.sub(r"\n{3,}", "\n\n", soup.get_text("\n", strip=True))
            # Harvest child links from this page (same domain or known platforms — for deep recursion)
            child_urls = []
            from urllib.parse import urlparse, urljoin
            base_domain = urlparse(final_url).netloc
            for a in soup.find_all("a", href=True)[:200]:
                href = a["href"]
                if href.startswith("#") or href.startswith("javascript:"): continue
                abs_url = urljoin(final_url, href)
                p = urlparse(abs_url)
                if not p.scheme.startswith("http"): continue
                # Keep same-domain links + Notion/Google Docs/specific platforms (typical "course module" pattern)
                if p.netloc == base_domain or any(d in p.netloc for d in ["notion.so","notion.com","docs.google","drive.google","airtable","gitbook"]):
                    child_urls.append(abs_url)
            # Dedup + cap at 20 children per page
            child_urls = list(dict.fromkeys(child_urls))[:20]
            return {"url": url, "final": final_url, "kind": "html",
                    "title": title, "text": body[:max_chars],
                    "truncated": len(body) > max_chars,
                    "child_urls": child_urls}
    except Exception as e:
        # 1 retry on transient
        if attempt < SCRAPE_RETRIES and not isinstance(e, (ValueError,)):
            await asyncio.sleep(1)
            return await fetch(session, url, max_chars, attempt+1)
        return {"url": url, "kind": "error",
                "note": f"{type(e).__name__}: {str(e)[:200]}", "child_urls": []}


async def scrape_recursive(urls, max_depth=SCRAPE_DEPTH):
    """BFS scrape: depth=0 → seed URLs, depth=1 → their child links, ..."""
    if not urls: return []
    import aiohttp
    seen = set()
    results = []
    frontier = [(u, 0) for u in urls]
    async with aiohttp.ClientSession() as session:
        while frontier:
            # Process current depth in parallel
            current = [(u, d) for (u, d) in frontier if u not in seen and d < max_depth]
            for u, _ in current: seen.add(u)
            if not current: break
            fetched = await asyncio.gather(*[fetch(session, u) for u, _ in current])
            # Tag depth + collect for output
            next_frontier = []
            for (u, depth), res in zip(current, fetched):
                res["depth"] = depth
                results.append(res)
                if depth + 1 < max_depth:
                    for cu in res.get("child_urls", [])[:10]:  # cap recursion fanout
                        if cu not in seen:
                            next_frontier.append((cu, depth + 1))
            frontier = next_frontier
    return results

# Back-compat alias
scrape_all = scrape_recursive


# ---------- doc compile ----------

def compile_doc(meta, transcript, frame_descs, scraped, comments, opts):
    md = []
    md.append("---")
    title_safe = json.dumps(meta.get("title",""))
    for k, v in [
        ("video_id", meta.get("id")),
        ("url", meta.get("webpage_url")),
        ("channel", meta.get("uploader", meta.get("channel"))),
        ("channel_handle", meta.get("uploader_id")),
        ("title", title_safe),
        ("upload_date", meta.get("upload_date")),
        ("duration_seconds", meta.get("duration")),
        ("view_count_at_scrape", meta.get("view_count")),
        ("like_count", meta.get("like_count")),
        ("comment_count_total", meta.get("comment_count")),
        ("comments_pulled", len(comments)),
        ("processed_at", time.strftime("%Y-%m-%d %H:%M:%S")),
        ("pipeline", "v4 max-speed-quality multi-provider"),
        ("vision_providers", "gemini×4 + groq + cerebras + qwen2.5vl-local + moondream-local"),
        ("asr_provider", "whisper.cpp metal base.en"),
        ("frames_kept", opts["frames_kept"]),
        ("frames_raw", opts["frames_raw"]),
        ("transcript_source", opts["transcript_source"]),
        ("urls_scraped", len(scraped)),
        ("processing_time_seconds", opts["elapsed_s"]),
    ]:
        md.append(f"{k}: {v}")
    md.append("---\n")
    md.append(f"# {meta.get('title','(no title)')}\n")
    md.append(f"> **{meta.get('uploader','?')}** • {meta.get('duration_string','?')} • uploaded {meta.get('upload_date','?')} • {meta.get('view_count','?')} views • {meta.get('like_count','?')} likes\n")
    md.append(f"Source: {meta.get('webpage_url')}\n")

    md.append("## Description (verbatim)\n```\n" + (meta.get("description","") or "(empty)") + "\n```\n")

    if scraped:
        md.append("## Linked sites — deep scrape\n")
        for s in scraped:
            md.append(f"### {s.get('title') or s.get('url')}")
            md.append(f"- URL: {s.get('url')}")
            if s.get("final") and s["final"] != s["url"]:
                md.append(f"- Final URL: {s['final']}")
            md.append(f"- Kind: {s.get('kind')}")
            if s.get("note"): md.append(f"- Note: {s['note']}")
            if s.get("text"):
                md.append("\n```\n" + s["text"] + "\n```")
                if s.get("truncated"): md.append("_(truncated)_")
            md.append("")

    if comments:
        md.append("## Comments — top with creator replies\n")
        for c in comments[:100]:
            author = c.get("author","?")
            txt = (c.get("text","") or "").strip().replace("\n", " ")
            likes = c.get("like_count", "?")
            tag = " **[CREATOR]**" if c.get("author_is_uploader") else ""
            md.append(f"- **{author}**{tag} ({likes} likes): {txt[:500]}")
            for reply in c.get("replies",[])[:5]:
                rtag = " **[CREATOR]**" if reply.get("author_is_uploader") else ""
                md.append(f"  - **{reply.get('author','?')}**{rtag}: {(reply.get('text','') or '').strip().replace(chr(10),' ')[:300]}")
        md.append("")

    md.append("## Full transcript\n")
    for seg in transcript or []:
        md.append(f"`{seg['start']}` {seg['text']}")
    md.append("")

    md.append("## Visual layer — per-frame descriptions\n")
    md.append(f"_Scene-change + 0.33fps base sampling, deduped, {opts['frames_kept']} unique frames at {RESOLUTION}px. Vision via multi-provider concurrent dispatch (Gemini × 4 + Groq + Cerebras + local fallbacks)._\n")
    for fd in frame_descs:
        md.append(f"### {fd['timestamp']}")
        md.append(fd["description"])
        md.append("")
    return "\n".join(md)


# ---------- main ----------

def process(url, handle, force=False):
    vid_id = video_id_from_url(url)
    if not vid_id:
        raise ValueError(url)
    out_dir = OUTPUT_ROOT / handle
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{vid_id}.md"
    if out_path.exists() and not force:
        head = out_path.read_text()[:500] if out_path.stat().st_size > 100 else ""
        if ("pipeline: v4" in head or "pipeline: v3" in head) and out_path.stat().st_size > 4096:
            log(f"skip: {out_path}")
            return out_path

    t0 = time.time()
    log(f"=== {url} ===", "main")
    meta, yt_captions, comments = yt_metadata(url)

    video_path = download_video(url, vid_id)

    # ALWAYS run Whisper — YouTube auto-captions are inaccurate.
    # Groq whisper-large-v3-turbo primary, whisper.cpp Metal local fallback.
    transcript = []
    transcript_source = None
    try:
        transcript, transcript_source = transcribe(video_path)
    except Exception as e:
        log(f"whisper failed: {e}", "whisper")

    # Only fall back to YouTube auto-captions if BOTH Whisper paths failed
    if not transcript and yt_captions:
        transcript = yt_captions
        transcript_source = "youtube_auto_captions_fallback"
        log("WARN: using YouTube auto-captions as last resort (Whisper failed)", "whisper")
    elif not transcript:
        transcript = []
        transcript_source = "FAILED"

    scene_frames, base_frames, frames_dir = extract_frames(video_path)
    unique_frames, adaptive_cap = dedupe_frames(scene_frames, base_frames, duration_sec=meta.get("duration",0))
    save_raw_frames(unique_frames, vid_id)
    log(f"frames: {len(scene_frames)} scene + {len(base_frames)} base → {len(unique_frames)} unique", "frames")
    frame_descs = describe_frames_concurrent(unique_frames, meta.get("duration", 0))

    # Pull URLs from description + transcript ("go to opbot.io") + frame descriptions ("on-screen: notion.so/xyz")
    urls = extract_urls_from_all(meta, transcript, frame_descs)
    log(f"extracted {len(urls)} URLs (description + transcript + on-screen text)", "urls")
    scraped = asyncio.run(scrape_all(urls)) if urls else []

    elapsed = int(time.time() - t0)
    doc = compile_doc(meta, transcript, frame_descs, scraped, comments, {
        "frames_kept": len(unique_frames),
        "frames_raw": len(scene_frames) + len(base_frames),
        "transcript_source": transcript_source,
        "elapsed_s": elapsed,
    })
    out_path.write_text(doc)
    log(f"SAVED {out_path.name} ({len(doc)//1024}KB) in {elapsed}s", "main")

    # cleanup
    try:
        if video_path.exists(): video_path.unlink()
        if frames_dir.exists(): shutil.rmtree(frames_dir)
        for ext in (".en.vtt", ".vtt", ".info.json"):
            p = TMP_ROOT / f"{vid_id}{ext}"
            if p.exists(): p.unlink()
    except Exception as e:
        log(f"cleanup warn: {e}")
    return out_path


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("handle")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    process(args.url, args.handle, force=args.force)
