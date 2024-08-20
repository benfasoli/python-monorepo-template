FROM python:3.12-slim-bookworm

ENV SERVICE_NAME=worker
ENV SERVICE_ROOT=services/${SERVICE_NAME}

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

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
CMD python -m src.worker
