"""Multi-provider vision pool — round-robin across free APIs with rate-limit fallback.

Providers (in priority order):
  1. Gemini 3.5-flash    (Google AI Studio, free 10-15 RPM)
  2. Gemini 2.5-flash    (free 10-15 RPM)
  3. Gemini flash-latest (free 10-15 RPM)
  4. Gemini flash-lite-latest (free 10-15 RPM)
  5. Groq Llama-4-Scout-17B-Vision (free 30 RPM)
  6. Cerebras Llama-3.3-70B + Llama-4-Scout (if vision available, free)
  7. Local qwen2.5-vl:7b (Ollama, unlimited but slow)
  8. Local moondream:1.8b (fastest local fallback)

Each provider tracks its own cooldown (set on 429). Pool picks first non-cooled.
Batch interface: send N frames in 1 request, parse "FRAME i: ..." lines.
"""
import base64
import io
import os
import re
import time
from typing import List


def load_env():
    """Load API keys from .env files into environment."""
    env_files = [
        os.path.expanduser("~/Documents/Claude/memory/.env"),
        os.path.expanduser("~/Documents/Claude/yt-deep-knowledge/_pipeline/.env"),
        "_pipeline/.env",
    ]
    for ef in env_files:
        if not os.path.exists(ef):
            continue
        for line in open(ef):
            line = line.strip()
            if line.startswith("export "):
                line = line[7:]
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                v = v.strip().strip("'\"")
                if v and k not in os.environ:
                    os.environ[k] = v


load_env()


BATCH_PROMPT = (
    "I'm sending you {n} consecutive frames from a YouTube video, in order. "
    "For EACH frame, output a 2-3 sentence description on its own line, prefixed with `FRAME {{i}}:` (i = 1-indexed). "
    "Include any on-screen text verbatim, who/what is visible, the setting, and any action/gesture. "
    "Be observable not interpretive. Do not skip any frame."
)


def parse_batch_output(text, n):
    """Parse 'FRAME 1: ...' lines into list of descriptions."""
    descs = {}
    cur_idx = None
    cur_buf = []
    for line in text.strip().split("\n"):
        m = re.match(r"^\s*\*?\*?FRAME\s+(\d+)\s*:?\*?\*?\s*(.*)$", line, re.IGNORECASE)
        if m:
            if cur_idx is not None:
                descs[cur_idx] = " ".join(cur_buf).strip()
            cur_idx = int(m.group(1))
            cur_buf = [m.group(2)]
        elif cur_idx is not None and line.strip():
            cur_buf.append(line.strip())
    if cur_idx is not None:
        descs[cur_idx] = " ".join(cur_buf).strip()
    return [descs.get(i, "[missing]") for i in range(1, n + 1)]


def is_rate_limit_error(exc):
    msg = str(exc).lower()
    return any(x in msg for x in ["429", "quota", "exceeded", "rate limit", "too many", "throttl"])


# ---------- Gemini provider ----------

class GeminiProvider:
    def __init__(self, model_name):
        self.model_name = model_name
        self.cooldown_until = 0.0
        if not os.environ.get("GOOGLE_API_KEY"):
            raise RuntimeError("GOOGLE_API_KEY not set")
        import google.generativeai as genai
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        self.model = genai.GenerativeModel(model_name)

    def describe_batch(self, frame_paths):
        from PIL import Image
        imgs = [Image.open(p) for p in frame_paths]
        n = len(imgs)
        prompt = BATCH_PROMPT.format(n=n)
        r = self.model.generate_content([prompt] + imgs, request_options={"timeout": 60})
        return parse_batch_output(r.text, n)

    @property
    def name(self):
        return f"gemini:{self.model_name}"


# ---------- Groq provider ----------

class GroqProvider:
    MAX_BATCH = 5  # Llama 4 Scout cap

    def __init__(self, model="meta-llama/llama-4-scout-17b-16e-instruct"):
        if not os.environ.get("GROQ_API_KEY"):
            raise RuntimeError("GROQ_API_KEY not set")
        from groq import Groq
        self.client = Groq()
        self.model = model
        self.cooldown_until = 0.0

    def describe_batch(self, frame_paths):
        # Chunk by MAX_BATCH if too large
        if len(frame_paths) > self.MAX_BATCH:
            out = []
            for i in range(0, len(frame_paths), self.MAX_BATCH):
                out.extend(self._call(frame_paths[i:i+self.MAX_BATCH]))
            return out
        return self._call(frame_paths)

    def _call(self, frame_paths):
        n = len(frame_paths)
        content = [{"type": "text", "text": BATCH_PROMPT.format(n=n)}]
        for p in frame_paths:
            b64 = base64.b64encode(open(p, "rb").read()).decode()
            content.append({"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}})
        r = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": content}],
            temperature=0,
            max_tokens=2000,
        )
        return parse_batch_output(r.choices[0].message.content, n)

    @property
    def name(self):
        return f"groq:{self.model.split('/')[-1][:20]}"


# ---------- Cerebras provider ----------

class CerebrasProvider:
    def __init__(self, model="llama-4-scout-17b-16e-instruct"):
        if not os.environ.get("CEREBRAS_API_KEY"):
            raise RuntimeError("CEREBRAS_API_KEY not set")
        from cerebras.cloud.sdk import Cerebras
        self.client = Cerebras()
        self.model = model
        self.cooldown_until = 0.0

    def describe_batch(self, frame_paths):
        n = len(frame_paths)
        content = [{"type": "text", "text": BATCH_PROMPT.format(n=n)}]
        for p in frame_paths:
            b64 = base64.b64encode(open(p, "rb").read()).decode()
            content.append({"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}})
        r = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": content}],
            temperature=0,
            max_tokens=2000,
        )
        return parse_batch_output(r.choices[0].message.content, n)

    @property
    def name(self):
        return f"cerebras:{self.model[:20]}"


# ---------- Local Ollama fallback ----------

class OllamaProvider:
    def __init__(self, model="qwen2.5vl:7b"):
        import ollama
        self.ollama = ollama
        self.model = model
        self.cooldown_until = 0.0

    def describe_batch(self, frame_paths):
        # Ollama doesn't reliably handle multi-image — fall back to single per call.
        out = []
        for p in frame_paths:
            img_b64 = base64.b64encode(open(p, "rb").read()).decode()
            r = self.ollama.chat(model=self.model,
                                 messages=[{"role": "user",
                                            "content": "Describe this frame in 2-3 sentences. Include any on-screen text verbatim, who/what is visible, the setting.",
                                            "images": [img_b64]}],
                                 options={"num_predict": 200})
            desc = r["message"]["content"].strip()
            desc = re.sub(r"^\[[\d.,\s]+\]\s*", "", desc)  # strip moondream bbox artifacts
            out.append(desc)
        return out

    @property
    def name(self):
        return f"ollama:{self.model}"


# ---------- Pool ----------

class VisionPool:
    def __init__(self):
        self.providers = []
        # Try Gemini endpoints
        for model in ["gemini-3.5-flash", "gemini-flash-latest", "gemini-2.5-flash", "gemini-flash-lite-latest"]:
            try:
                self.providers.append(GeminiProvider(model))
            except Exception as e:
                print(f"[vision_pool] skip {model}: {e}")
        # Try Groq
        try:
            self.providers.append(GroqProvider())
        except Exception as e:
            print(f"[vision_pool] skip groq: {e}")
        # Cerebras: no vision model on free tier as of 2026-05; key kept for future
        # text post-processing (summarization, fact-check) where their 1000+ tok/s wins.
        # Skip from vision pool entirely.
        # Always have local fallback
        try:
            self.providers.append(OllamaProvider("qwen2.5vl:7b"))
        except Exception as e:
            print(f"[vision_pool] skip ollama qwen: {e}")
        try:
            self.providers.append(OllamaProvider("moondream"))
        except Exception as e:
            print(f"[vision_pool] skip ollama moondream: {e}")
        self.cursor = 0
        print(f"[vision_pool] ready with {len(self.providers)} providers: " +
              ", ".join(p.name for p in self.providers))

    def describe_batch(self, frame_paths, max_retries=3):
        """Try each non-cooled provider in round-robin order. Returns list of descriptions."""
        last_err = None
        attempts = 0
        max_attempts = len(self.providers) * max_retries
        while attempts < max_attempts:
            now = time.time()
            idx = self.cursor % len(self.providers)
            self.cursor += 1
            attempts += 1
            p = self.providers[idx]
            if p.cooldown_until > now:
                continue
            try:
                t0 = time.time()
                result = p.describe_batch(frame_paths)
                # Sanity: should be exactly len(frame_paths) descriptions
                if len(result) == len(frame_paths) and all(d and len(d) > 5 for d in result):
                    return result, p.name, time.time() - t0
                # Partial result — accept anyway if at least 1/2 good
                if sum(1 for d in result if d and len(d) > 5) >= len(frame_paths) // 2:
                    return result, p.name, time.time() - t0
                # Bad parse — try next provider
                continue
            except Exception as e:
                last_err = (p.name, e)
                if is_rate_limit_error(e):
                    p.cooldown_until = time.time() + 30
                else:
                    # Other error — short cooldown
                    p.cooldown_until = time.time() + 5
                continue
        raise RuntimeError(f"all vision providers exhausted; last error: {last_err}")


# Singleton
_POOL = None
def get_pool():
    global _POOL
    if _POOL is None:
        _POOL = VisionPool()
    return _POOL


if __name__ == "__main__":
    import sys
    pool = get_pool()
    if len(sys.argv) > 1:
        frames = sys.argv[1:]
        result, provider, elapsed = pool.describe_batch(frames)
        print(f"\n=== via {provider} in {elapsed:.1f}s ===")
        for i, d in enumerate(result):
            print(f"\n[FRAME {i+1}] {d}")
