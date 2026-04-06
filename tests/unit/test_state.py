"""Tests for state models."""

from src.state import ContentCalendar, PlannedPost, PostDraft, WeeklyReport


def test_planned_post_defaults():
    post = PlannedPost(platform="linkedin", theme="vision")
    assert post.product_id is None
    assert post.hook_idea == ""
    assert post.format == "text_plus_image"


def test_content_calendar_empty():
    cal = ContentCalendar(week="2026-W13")
    assert cal.posts == []
    assert cal.week == "2026-W13"


def test_content_calendar_with_posts(sample_calendar):
    assert len(sample_calendar.posts) == 4
    assert sample_calendar.posts[0].platform == "linkedin"
    assert sample_calendar.posts[1].product_id == "orch-v2"


def test_post_draft_status_flow():
    draft = PostDraft(platform="x", theme="vision", day="monday")
    assert draft.status == "planned"

    draft.status = "drafted"
    assert draft.status == "drafted"

    draft.status = "optimized"
    draft.status = "approved"
    draft.status = "posted"
    assert draft.status == "posted"


def test_post_draft_serialization():
    draft = PostDraft(
        platform="linkedin",
        theme="product",
        product_focus="orch-v2",
        day="tuesday",
        text="Hello world",
        hashtags=["AI", "Tech"],
        cta="Try it now",
    )
    data = draft.model_dump()
    assert data["platform"] == "linkedin"
    assert data["hashtags"] == ["AI", "Tech"]
    assert data["status"] == "planned"


def test_weekly_report():
    report = WeeklyReport(
        week="2026-W13",
        total_posts_planned=16,
        total_posts_drafted=16,
        total_posts_approved=14,
    )
    assert report.total_posts_posted == 0
    assert report.notes == ""