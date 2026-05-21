#!/usr/bin/env python3
"""Process a chunk of the video queue. Used by GitHub Actions matrix workers."""
import argparse, sys, time
from pathlib import Path

# Add pipeline dir to path
sys.path.insert(0, str(Path(__file__).parent))
import process_video


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--queue", required=True)
    ap.add_argument("--chunk-index", type=int, required=True)
    ap.add_argument("--total-chunks", type=int, required=True)
    ap.add_argument("--output-dir", required=True)
    args = ap.parse_args()

    rows = [line.rstrip("\n").split("\t") for line in open(args.queue) if line.strip()]
    chunk = [r for i, r in enumerate(rows) if i % args.total_chunks == args.chunk_index]
    print(f"[chunk {args.chunk_index}/{args.total_chunks}] processing {len(chunk)} videos")

    out_root = Path(args.output_dir)
    out_root.mkdir(parents=True, exist_ok=True)
    process_video.OUTPUT_ROOT = out_root  # redirect output

    t0 = time.time()
    ok = fail = 0
    for i, (handle, url) in enumerate(chunk, 1):
        try:
            process_video.process(url, handle, force=False)
            ok += 1
        except Exception as e:
            print(f"[chunk {args.chunk_index}] FAIL {url}: {e}")
            fail += 1
        if i % 5 == 0:
            elapsed = time.time() - t0
            rate = i / elapsed if elapsed else 0
            eta = (len(chunk) - i) / rate if rate else 0
            print(f"[chunk {args.chunk_index}] {i}/{len(chunk)} ok={ok} fail={fail} rate={rate:.2f}/s eta={eta/60:.0f}min")
    print(f"[chunk {args.chunk_index}] DONE ok={ok} fail={fail} in {(time.time()-t0)/60:.1f}min")


if __name__ == "__main__":
    main()
