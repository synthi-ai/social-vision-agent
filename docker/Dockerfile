### Stage 1 — Install dependencies with uv
FROM python:3.12-slim AS builder

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy dependency manifests first for layer caching
COPY pyproject.toml uv.lock ./

# Install production dependencies only (no dev deps)
RUN uv sync --frozen --no-dev --no-install-project

# Copy application source
COPY . .

# Install the project itself
RUN uv sync --frozen --no-dev


### Stage 2 — Slim runtime
FROM python:3.12-slim AS runtime

WORKDIR /app

# System deps for runtime (curl for healthcheck, libpq for psycopg)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Copy the virtual environment from builder
COPY --from=builder /app/.venv /app/.venv

# Copy application code
COPY --from=builder /app /app

# Ensure venv binaries are on PATH
ENV PATH="/app/.venv/bin:$PATH"

# Create writable directories
RUN mkdir -p /app/output /app/images

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD curl -sf http://localhost:8000/ || exit 1

# Default: run the API server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
