"""Shared test fixtures."""

from __future__ import annotations

import pytest

from src.state import (
    AgentState,
    ContentCalendar,
    PlannedPost,
    PostDraft,
)


@pytest.fixture
def sample_vision() -> str:
    return "We build AI-powered developer tools. Local-first, multi-model, open-core."


@pytest.fixture
def sample_calendar() -> ContentCalendar:
    return ContentCalendar(
        week="2026-W13",
        posts=[
            PlannedPost(
                platform="linkedin",
                theme="vision",
                hook_idea="Why local-first AI matters more than ever",
                format="single_image",
                day="tuesday",
            ),
            PlannedPost(
                platform="x",
                theme="product",
                product_id="orch-v2",
                hook_idea="Ship 3x faster with intelligent model routing",
                format="thread",
                day="wednesday",
            ),
            PlannedPost(
                platform="tiktok",
                theme="education",
                hook_idea="What is model fallback and why you need it",
                format="reel_15_60s",
                day="thursday",
            ),
            PlannedPost(
                platform="facebook",
                theme="engagement",
                hook_idea="What's your biggest pain point with AI in production?",
                format="single_image",
                day="friday",
            ),
        ],
    )


@pytest.fixture
def sample_drafts() -> list[PostDraft]:
    return [
        PostDraft(
            platform="linkedin",
            theme="vision",
            day="tuesday",
            text="Local-first AI is not just a trend. It's the future.",
            hashtags=["AI", "LocalFirst", "DevTools"],
            cta="What do you think? Share your experience below.",
            status="drafted",
        ),
        PostDraft(
            platform="x",
            theme="product",
            product_focus="orch-v2",
            day="wednesday",
            text="Ship 3x faster with Orchestrator v2.",
            hashtags=["AI", "MLOps"],
            cta="Try it free",
            status="drafted",
        ),
    ]


@pytest.fixture
def sample_state(sample_vision, sample_calendar, sample_drafts) -> AgentState:
    return AgentState(
        messages=[],
        current_week="2026-W13",
        vision_summary=sample_vision,
        research_insights="",
        calendar=sample_calendar,
        product_spotlights={},
        drafts=sample_drafts,
        approved_drafts=[],
        report=None,
        error=None,
    )
