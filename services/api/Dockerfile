FROM python:3.12-slim-bookworm

ENV SERVICE_NAME=api
ENV SERVICE_ROOT=services/${SERVICE_NAME}
ENV PORT=8080

WORKDIR /app

COPY . .
RUN --mount=from=ghcr.io/astral-sh/uv:0.2.37,source=/uv,target=/bin/uv \
    uv sync \
    --no-cache \
    --no-dev \
    --locked \
    --python=/usr/local/bin/python \
    --package=${SERVICE_NAME}

# TODO: install uv dependencies to system environment once supported
#   https://github.com/astral-sh/uv/issues/5964
ENV PATH=".venv/bin:${PATH}"

ENV PYTHONPATH=${SERVICE_ROOT}
CMD uvicorn src.api.main:app \
    --host=0.0.0.0 \
    --port=${PORT}
