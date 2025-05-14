FROM python:3.13-slim-bookworm

ENV SERVICE_NAME=worker
ENV SERVICE_ROOT=src/${SERVICE_NAME}

WORKDIR /src

COPY . .
RUN --mount=from=ghcr.io/astral-sh/uv:0.5.29,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    uv sync \
    --compile-bytecode \
    --locked \
    --no-dev \
    --package=${SERVICE_NAME} \
    --python-preference=only-system

ENV PATH=".venv/bin:${PATH}"
ENV PYTHONPATH=${SERVICE_ROOT}

CMD ["python", "-m", "src.worker"]
