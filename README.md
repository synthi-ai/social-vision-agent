# Social Vision Agents

Production-ready social media content automation powered by LangGraph + Llama 4.

## Architecture

```
social-vision-agents/
├── config/
│   ├── settings.py              # Pydantic Settings v2 (env + PostgreSQL + LLM)
│   ├── platforms.yaml           # Platform rules (LinkedIn/X/TikTok/Facebook)
│   └── weekly_brief.yaml        # Weekly campaigns, image URLs, post counts
├── knowledge/
│   ├── vision.md                # Company vision (customize this)
│   └── products.yaml            # Product catalog
├── src/
│   ├── state.py                 # TypedDict state with 8 fields
│   ├── utils/
│   │   ├── llm_factory.py       # Ollama + Groq + Gemini fallback factory
│   │   ├── json_parser.py       # Shared JSON parser for LLM outputs
│   │   └── logger.py            # structlog (JSON in prod, color in dev)
│   ├── tools/
│   │   ├── product_knowledge.py # Product RAG from YAML
│   │   ├── platform_rules.py    # Platform constraints reader
│   │   ├── weekly_brief.py      # Weekly brief loader + image URL resolver
│   │   ├── web_search.py        # Tavily (primary) + DuckDuckGo (fallback)
│   │   └── grok_imagine.py      # Optional image generation fallback
│   ├── agents/                  # 6 specialized agents
│   │   ├── strategist.py        # Dynamic calendar from weekly brief
│   │   ├── product_expert.py    # Product spotlight enrichment
│   │   ├── writer.py            # Multi-platform copywriting
│   │   ├── visual.py            # Visual prompts + image URL assignment
│   │   ├── optimizer.py         # Platform constraint optimization
│   │   └── publisher.py         # Export + PostgreSQL save
│   ├── graph/
│   │   ├── nodes.py             # 8 LangGraph nodes with error recovery
│   │   └── weekly_content_graph.py  # Graph compilation + interrupt
│   └── db/
│       └── postgres.py          # asyncpg async CRUD (posts + batches)
├── skills/
│   └── public/                  # 7 ultra-detailed skill files
├── main.py                      # FastAPI API (run/approve/posts/images/upload)
├── run_weekly.py                # CLI entry point
├── scheduler.py                 # APScheduler (Monday 8AM cron)
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml       # Ollama + PostgreSQL + App
├── tests/                       # Unit + integration tests
├── pyproject.toml               # All deps (uv/hatch compatible)
├── .env.example                 # Config template
└── .gitignore
```

## Key Features

| Feature | Implementation |
|---|---|
| Images from config | `weekly_brief.yaml` → `image_urls` per campaign per platform |
| Multiple products/week | Campaigns list in weekly brief, dynamic post count |
| Web research | Tavily (primary) + DuckDuckGo (fallback) search |
| PostgreSQL storage | asyncpg driver, tables: `posts` + `weekly_batches` |
| LLM providers | Ollama (local), Groq (cloud), Gemini (cloud) with auto-fallback |
| DeerFlow patterns | Error recovery, structured logging, factory agents, thread isolation |
| Externalized config | 4 YAML files + `.env`, nothing hardcoded |
| Skills system | 7 detailed skill files injected into agent prompts |

## Quick Start

```bash
cp .env.example .env           # Fill in your keys
uv sync                        # Install dependencies
python run_weekly.py            # Run the pipeline
# or
uvicorn main:app --reload      # Start the API
```

## LLM Providers

| Provider | Config | Use Case |
|----------|--------|----------|
| Ollama | `OLLAMA_BASE_URL`, `OLLAMA_MODEL` | Local inference (default) |
| Groq | `GROQ_API_KEY`, `GROQ_FALLBACK_MODEL` | Cloud fallback |
| Gemini | `GOOGLE_API_KEY`, `GEMINI_MODEL` | Google AI alternative |

## Web Search

Tavily is the primary search provider (requires `TAVILY_API_KEY`).
DuckDuckGo is used as a free fallback when Tavily is unavailable.

## Docker

```bash
cd docker
docker compose up -d
```

Runs Ollama + PostgreSQL + FastAPI app + scheduler.
