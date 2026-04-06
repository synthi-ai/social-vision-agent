"""Shared JSON parser for LLM outputs.

Strips markdown code fences and parses JSON with graceful error handling.
Used by all agent modules that parse structured LLM responses.
"""

from __future__ import annotations

import json
import re
from typing import Any

import structlog

logger = structlog.get_logger(__name__)

_FENCE_RE = re.compile(r"^```(?:json)?\s*\n?", re.MULTILINE)


def strip_fences(text: str) -> str:
    """Remove markdown code fences (```json ... ```) from text."""
    return _FENCE_RE.sub("", text).strip().rstrip("`").strip()


def parse_json(raw_output: str, *, default: Any = None) -> Any:
    """Strip fences and parse JSON from raw LLM output.

    Args:
        raw_output: Raw text from an LLM response.
        default: Value to return if parsing fails.

    Returns:
        Parsed JSON object, or *default* on failure.
    """
    text = strip_fences(raw_output.strip())
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError) as exc:
        logger.warning("json_parser.failed", error=str(exc), preview=text[:120])
        return default
