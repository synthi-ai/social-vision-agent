"""Product knowledge tool — reads from products.yaml for RAG-style product enrichment."""

from __future__ import annotations

from pathlib import Path

import yaml
from langchain_core.tools import tool

from config.settings import settings


def _load_products() -> list[dict]:
    """Load the product catalog from YAML."""
    path = settings.KNOWLEDGE_DIR / "products.yaml"
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("products", [])


@tool
def get_product_info(product_id: str) -> str:
    """Retrieve detailed information about a product by its ID or name.

    Args:
        product_id: The product ID (e.g. 'orch-v2') or product name.

    Returns:
        YAML-formatted product details, or an error message if not found.
    """
    products = _load_products()

    for prod in products:
        if prod.get("id") == product_id or prod.get("name") == product_id:
            return yaml.dump(prod, allow_unicode=True, sort_keys=False, default_flow_style=False)

    available = [p.get("id", "unknown") for p in products]
    return f"Product '{product_id}' not found. Available: {', '.join(available)}"


@tool
def list_products() -> str:
    """List all available products with their ID, name, and status.

    Returns:
        A formatted summary of all products in the catalog.
    """
    products = _load_products()
    if not products:
        return "No products found in knowledge/products.yaml"

    lines = []
    for p in products:
        lines.append(f"- {p['id']}: {p['name']} [{p.get('status', 'unknown')}]")
        lines.append(f"  {p.get('short_description', '').strip()}")
    return "\n".join(lines)