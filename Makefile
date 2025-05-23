.PHONY: help
help:  ## Show available options
	@echo
	@echo "\033[1mUsage\033[0m: make <COMMAND>\n"
	@echo "\033[1mCommands\033[0m:\n"
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build:  ## Build docker images configured in compose.yaml
	@docker compose build

.PHONY: clean
clean:  ## Remove development artifacts
	@rm -rf `find . -name .venv`
	@rm -f `find . -name .coverage`
	@rm -rf `find . -name .pdm-build`
	@rm -rf `find . -name .pytest_cache`
	@rm -rf `find . -name .ruff_cache`
	@rm -f `find . -name '*.pyc'`
	@rm -f `find . -name '*.pyo'`

.PHONY: dev
dev:  ## Build and run each service in a local docker container
	@docker compose up --build --remove-orphans

.PHONY: dev-infra
dev-infra:  ## Start local development infra in docker containers
	@docker compose up -d --remove-orphans db

.PHONY: install
install:  ## Install dependencies and refresh lockfile
	@uv sync

.PHONY: format
format:  ## Format code overwriting if necessary
	@uv run -- ruff format

.PHONY: lint
lint:  ## Run static analysis checks for all packages
	@uv run -- ruff format --check
	@uv run -- ruff check
	@uv run -- pyright

.PHONY: test
test: dev-infra  ## Run tests for all packages
	@uv run -- pytest --cov-report=term-missing --cov .
