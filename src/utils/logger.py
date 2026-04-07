"""Structured JSON logging configuration with structlog.

Dev mode: colored console output.
Prod mode: pure JSON (compatible with ELK, Datadog, etc.).
"""

from __future__ import annotations

import os
import sys

import structlog


def setup_logging(json_output: bool | None = None) -> None:
    """Configure structlog for the entire application.

    Args:
        json_output: Force JSON if True. If None, auto-detects
                     (JSON when no TTY = production/Docker).
    """
    if json_output is None:
        json_output = not sys.stderr.isatty()

    shared_processors: list[structlog.types.Processor] = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.UnicodeDecoder(),
    ]

    if json_output:
        renderer: structlog.types.Processor = structlog.processors.JSONRenderer()
    else:
        renderer = structlog.dev.ConsoleRenderer(colors=True)

    structlog.configure(
        processors=[
            *shared_processors,
            structlog.processors.format_exc_info,
            renderer,
        ],
        wrapper_class=structlog.make_filtering_bound_logger(
            int(os.environ.get("LOG_LEVEL", "20"))  # 20 = INFO
        ),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )
