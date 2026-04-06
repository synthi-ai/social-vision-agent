"""Tests for tools (product knowledge, platform rules)."""

from __future__ import annotations

from src.tools.product_knowledge import get_product_info, list_products
from src.tools.platform_rules import get_platform_rules, get_all_platform_rules


def test_list_products():
    result = list_products.invoke({})
    assert "orch-v2" in result
    assert "studio-agents" in result
    assert "obs-realtime" in result


def test_get_product_info_by_id():
    result = get_product_info.invoke({"product_id": "orch-v2"})
    assert "Orchestrator" in result
    assert "routing" in result.lower() or "Routing" in result


def test_get_product_info_not_found():
    result = get_product_info.invoke({"product_id": "nonexistent"})
    assert "not found" in result.lower()
    assert "orch-v2" in result  # Should list available products


def test_get_platform_rules_linkedin():
    result = get_platform_rules.invoke({"platform": "linkedin"})
    assert "linkedin" in result.lower()
    assert "3000" in result  # max_length


def test_get_platform_rules_unknown():
    result = get_platform_rules.invoke({"platform": "myspace"})
    assert "not found" in result.lower()


def test_get_all_platform_rules():
    result = get_all_platform_rules.invoke({})
    assert "linkedin" in result
    assert "tiktok" in result
    assert "facebook" in result