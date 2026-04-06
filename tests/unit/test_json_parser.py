"""Tests for the shared JSON parser utility."""

from src.utils.json_parser import parse_json, strip_fences


def test_strip_json_fences():
    """Remove ```json ... ``` fences."""
    raw = '```json\n{"key": "value"}\n```'
    assert strip_fences(raw) == '{"key": "value"}'


def test_strip_plain_fences():
    """Remove ``` ... ``` fences without language tag."""
    raw = '```\n[1, 2, 3]\n```'
    assert strip_fences(raw) == "[1, 2, 3]"


def test_strip_no_fences():
    """Pass through text without fences unchanged."""
    raw = '{"already": "clean"}'
    assert strip_fences(raw) == raw


def test_parse_json_valid():
    """Parse valid JSON from fenced LLM output."""
    raw = '```json\n{"posts": [1, 2]}\n```'
    result = parse_json(raw)
    assert result == {"posts": [1, 2]}


def test_parse_json_plain():
    """Parse valid JSON without fences."""
    raw = '  [{"a": 1}]  '
    result = parse_json(raw)
    assert result == [{"a": 1}]


def test_parse_json_invalid_returns_default():
    """Return default on invalid JSON."""
    result = parse_json("not json at all", default={"posts": []})
    assert result == {"posts": []}


def test_parse_json_default_none():
    """Return None when default is not specified and parsing fails."""
    result = parse_json("broken")
    assert result is None


def test_parse_json_empty_string():
    """Handle empty string gracefully."""
    result = parse_json("", default=[])
    assert result == []


def test_parse_json_nested_fences():
    """Handle output with extra whitespace around fences."""
    raw = '\n  ```json\n  {"nested": true}\n  ```\n  '
    result = parse_json(raw)
    assert result == {"nested": True}
