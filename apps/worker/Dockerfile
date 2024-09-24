FROM python:3.12-slim-bookworm

ENV SERVICE_NAME=worker
ENV SERVICE_ROOT=services/${SERVICE_NAME}

WORKDIR /app

COPY . .
RUN --mount=from=ghcr.io/astral-sh/uv:0.4.15,source=/uv,target=/bin/uv \
    uv sync \
    --locked \
    --no-cache \
    --no-dev \
    --package=${SERVICE_NAME} \
    --python=/usr/local/bin/python

ENV PATH=".venv/bin:${PATH}"
ENV PYTHONPATH=${SERVICE_ROOT}

CMD python -m src.worker
