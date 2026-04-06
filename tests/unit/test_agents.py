"""Tests for agent parsing functions (no LLM calls)."""

from __future__ import annotations

from src.agents.strategist import parse_calendar
from src.agents.product_expert import extract_product_ids, parse_spotlights
from src.agents.writer import parse_drafts
from src.agents.visual import parse_visual_prompts, merge_visual_into_drafts
from src.agents.optimizer import parse_optimized, merge_optimized_into_drafts
from src.state import ContentCalendar, PlannedPost, PostDraft


def test_parse_calendar_valid_json():
    raw = '''
    {
        "week": "2026-W13",
        "posts": [
            {
                "platform": "linkedin",
                "theme": "vision",
                "product_id": null,
                "hook_idea": "Why AI needs to be local-first",
                "format": "carousel",
                "day": "monday"
            }
        ]
    }
    '''
    cal = parse_calendar(raw, "2026-W13")
    assert len(cal.posts) == 1
    assert cal.posts[0].platform == "linkedin"
    assert cal.posts[0].product_id is None


def test_parse_calendar_with_markdown_fences():
    raw = '```json\n{"week": "2026-W13", "posts": []}\n```'
    cal = parse_calendar(raw, "2026-W13")
    assert cal.week == "2026-W13"
    assert cal.posts == []


def test_parse_calendar_invalid_json():
    cal = parse_calendar("not json at all", "2026-W13")
    assert cal.posts == []


def test_extract_product_ids(sample_calendar):
    ids = extract_product_ids(sample_calendar)
    assert "orch-v2" in ids


def test_parse_spotlights():
    raw = '{"orch-v2": {"name": "Orchestrator", "key_benefit": "Fast"}}'
    result = parse_spotlights(raw)
    assert "orch-v2" in result
    assert result["orch-v2"]["name"] == "Orchestrator"


def test_parse_drafts():
    raw = '''[
        {
            "platform": "linkedin",
            "theme": "vision",
            "day": "tuesday",
            "text": "Hello world",
            "hashtags": ["AI"],
            "cta": "Share!"
        }
    ]'''
    drafts = parse_drafts(raw)
    assert len(drafts) == 1
    assert drafts[0].platform == "linkedin"
    assert drafts[0].status == "drafted"


def test_parse_visual_prompts():
    raw = '[{"platform": "linkedin", "day": "tuesday", "visual_prompt": "A futuristic server room"}]'
    result = parse_visual_prompts(raw)
    assert len(result) == 1
    assert "server room" in result[0]["visual_prompt"]


def test_merge_visual_into_drafts():
    drafts = [PostDraft(platform="linkedin", theme="vision", day="tuesday")]
    visuals = [{"platform": "linkedin", "day": "tuesday", "visual_prompt": "Tech art"}]
    merged = merge_visual_into_drafts(drafts, visuals)
    assert merged[0].visual_prompt == "Tech art"


def test_parse_optimized():
    raw = '[{"platform": "x", "day": "monday", "optimized_text": "Better text", "hashtags": ["AI"], "cta": "Go", "optimization_notes": "Shortened"}]'
    result = parse_optimized(raw)
    assert len(result) == 1
    assert result[0]["optimized_text"] == "Better text"


def test_merge_optimized_into_drafts():
    drafts = [PostDraft(platform="x", theme="vision", day="monday", text="Original")]
    optimized = [{"platform": "x", "day": "monday", "optimized_text": "Improved", "hashtags": ["AI"], "cta": "Go", "optimization_notes": "Fixed"}]
    merged = merge_optimized_into_drafts(drafts, optimized)
    assert merged[0].optimized_text == "Improved"
    assert merged[0].status == "optimized"