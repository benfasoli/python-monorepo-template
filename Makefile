export DOCKER_DEFAULT_PLATFORM=linux/amd64

.PHONY: all
all: clean install format lint test

.PHONY: build
build:
	docker compose -f docker/build/compose.yaml build

.PHONY: build
dev: build
	docker compose -f docker/build/compose.yaml up

.PHONY: clean
clean:
	rm -f `find . -name .coverage`
	rm -rf `find . -name .pdm-build`
	rm -rf `find . -name .pdm-python`
	rm -rf `find . -name .pytest_cache`
	rm -rf `find . -name .ruff_cache`
	rm -rf `find . -name .venv`
	rm -f `find . -name '*.pyc'`
	rm -f `find . -name '*.pyo'`

.PHONY: infra-local
infra-local:
	docker stop `docker ps -aq`
	docker compose up --detach --remove-orphans

.PHONY: install
install:
	uv sync

.PHONY: format
format:
	uv run -- ruff format

.PHONY: lint
lint:
	uv run -- ruff format --check
	uv run -- ruff check
	uv run -- pyright

.PHONY: test
test:
	uv run -- pytest --cov-report=term-missing --cov .
