"""Grok Imagine tool — generates images via xAI's image generation API."""

from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime

import httpx
import structlog
from langchain_core.tools import tool

from config.settings import settings

logger = structlog.get_logger(__name__)


@tool
def generate_image(prompt: str, filename_hint: str = "post") -> str:
    """Generate an image using the Grok Imagine API (xAI).

    Args:
        prompt: Detailed visual description for the image to generate.
        filename_hint: Short label for the output filename (e.g. 'linkedin_vision').

    Returns:
        Path to the saved image file, or an error/skip message.
    """
    config = settings.grok_imagine

    if not config.enabled:
        logger.info("grok_imagine.disabled", prompt_preview=prompt[:80])
        return f"[IMAGE_SKIP] Image generation disabled. Prompt saved: {prompt}"

    if config.api_key is None:
        return "[IMAGE_ERROR] GROK_IMAGINE_API_KEY not set in .env"

    output_dir = settings.OUTPUT_DIR / "images"
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_hint = "".join(c if c.isalnum() or c in "-_" else "_" for c in filename_hint)

    try:
        response = httpx.post(
            config.endpoint,
            headers={
                "Authorization": f"Bearer {config.api_key.get_secret_value()}",
                "Content-Type": "application/json",
            },
            json={
                "model": config.model,
                "prompt": prompt,
                "n": 1,
                "size": "1024x1024",
            },
            timeout=60.0,
        )
        response.raise_for_status()
        data = response.json()

        image_url = data.get("data", [{}])[0].get("url", "")
        if not image_url:
            return f"[IMAGE_ERROR] No image URL in API response: {json.dumps(data)[:200]}"

        # Download the image
        img_response = httpx.get(image_url, timeout=30.0)
        img_response.raise_for_status()

        filepath = output_dir / f"{safe_hint}_{timestamp}.png"
        filepath.write_bytes(img_response.content)

        logger.info("grok_imagine.success", filepath=str(filepath))
        return str(filepath)

    except httpx.HTTPStatusError as e:
        logger.error("grok_imagine.http_error", status=e.response.status_code)
        return f"[IMAGE_ERROR] API returned {e.response.status_code}: {e.response.text[:200]}"
    except Exception as e:
        logger.error("grok_imagine.error", error=str(e))
        return f"[IMAGE_ERROR] {type(e).__name__}: {e}"