.PHONY: all
all: install format lint test

.PHONY: clean
clean:
	$(MAKE) -f ../../Makefile $@

.PHONY: install
install:
	pdm install --group :all

.PHONY: format
format:
	pdm run ruff format lib tests

.PHONY: lint
lint:
	pdm run ruff format --check .
	pdm run ruff check .
	pdm run mypy .

.PHONY: test
test:
	pdm run pytest --cov-report=term-missing --cov=.
