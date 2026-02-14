FROM python:3.14-slim-bookworm

ENV PACKAGE=api
ENV PORT=8000

# Set uv behavior for production installs.
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV UV_NO_DEV=1
ENV UV_NO_EDITABLE=1
ENV UV_NO_MANAGED_PYTHON=1
ENV UV_NO_SYNC=1
ENV UV_SYSTEM_PYTHON=1

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN --mount=from=ghcr.io/astral-sh/uv:0.10.2,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-workspace --package=${PACKAGE}

COPY . .
RUN --mount=from=ghcr.io/astral-sh/uv:0.10.2,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --package=${PACKAGE}

ENV PATH="/app/.venv/bin:$PATH"
CMD ["python", "-m", "api"]
