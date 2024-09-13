export DOCKER_DEFAULT_PLATFORM=linux/amd64

.PHONY: help
help:  ## Show available options.
	@echo
	@echo "\033[1mUsage\033[0m: make <COMMAND>\n"
	@echo "\033[1mCommands\033[0m:\n"
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build:  ## Build docker image for each service
	docker compose build

.PHONY: dev
dev: build  ## Build and run each service in a local docker container
	docker compose up

.PHONY: clean
clean:  ## Remove development artifacts
	rm -f `find . -name .coverage`
	rm -rf `find . -name .pdm-build`
	rm -rf `find . -name .pytest_cache`
	rm -rf `find . -name .ruff_cache`
	rm -rf `find . -name .venv`
	rm -f `find . -name '*.pyc'`
	rm -f `find . -name '*.pyo'`

.PHONY: install
install:  ## Install dependencies in .venv and refresh lockfile
	uv sync

.PHONY: infra
infra:  ## Start local development infra in docker containers
	docker compose up db

.PHONY: format
format:  ## Format code overwriting if necessary
	uv run -- ruff format

.PHONY: lint
lint:  ## Run static analysis checks for all packages and services
	uv run -- ruff format --check
	uv run -- ruff check
	uv run -- pyright

.PHONY: test
test:  ## Run tests for all packages and services
	uv run -- pytest --cov-report=term-missing --cov .
