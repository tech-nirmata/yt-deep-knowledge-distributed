# yt-deep-knowledge — distributed video processing

Process 3,092 videos across 20 free GitHub Actions runners in parallel.
Target: ~6 hours wall time for the full corpus (~10x speedup over local-only).

## Setup (one-time, ~5 min)

```bash
# 1. Create a public GitHub repo (e.g. yt-deep-knowledge)
# 2. From this directory:
cd /Users/parthnaria/Documents/Claude/yt-deep-knowledge-distributed
git init
git add .
git commit -m "initial scaffold"
git branch -M main
git remote add origin https://github.com/<your-username>/yt-deep-knowledge.git
git push -u origin main

# 3. Add repository secrets at:
#    https://github.com/<your-username>/yt-deep-knowledge/settings/secrets/actions
#
#    GOOGLE_API_KEY  — your Gemini key (already in .env)
#    GROQ_API_KEY    — from console.groq.com
#    CEREBRAS_API_KEY — from cloud.cerebras.ai
```

## Run

```bash
# Trigger the workflow:
gh workflow run "Process video chunks"

# Or via UI: Actions tab → "Process video chunks" → "Run workflow"
```

## How it works

- 3,092 videos split into 20 chunks of ~155 videos each.
- 20 GitHub Actions runners process chunks in parallel (free tier limit).
- Each runner installs ffmpeg + whisper.cpp + Python deps, then loops its chunk.
- Per-video: yt-dlp metadata → caption fetch → download → whisper.cpp (if no caption) → frame extract → multi-provider vision (Gemini × 4 + Groq + Cerebras) → async URL scrape → comment pull → markdown compile.
- Each runner uploads its chunk's markdown docs as an artifact.

## Retrieve results

```bash
# After workflow completes:
gh run list --workflow="Process video chunks" --limit 1
gh run download <RUN_ID>
# All chunks land in ./docs-chunk-0/, ./docs-chunk-1/, etc.

# Merge into local docs:
mkdir -p ~/Documents/Claude/yt-deep-knowledge
rsync -av docs-chunk-*/ ~/Documents/Claude/yt-deep-knowledge/
```

## Cost

100% free:
- GitHub Actions: 20 parallel runners on free tier, 2000 min/month
- Gemini, Groq, Cerebras: free API tiers
- whisper.cpp + ffmpeg + yt-dlp: open source

## Files

- `.github/workflows/process-videos.yml` — workflow with 20-way matrix
- `pipeline/process_video.py` — per-video processor (v4 stack)
- `pipeline/vision_pool.py` — multi-provider vision router
- `pipeline/process_chunk.py` — chunk dispatcher invoked by each runner
- `queue/all-videos.tsv` — 3,092 (handle, url) pairs, sharded by index mod 20
