.PHONY: all
all: clean install format lint test

.PHONY: build
build:
	docker compose -f docker/compose.build.yaml build

.PHONY: clean
clean:
	rm -f `find . -name .coverage`
	rm -rf `find . -name .mypy_cache`
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
	$(MAKE) -C lib/core $@
	$(MAKE) -C lib/dtos $@
	$(MAKE) -C services/api $@
	$(MAKE) -C services/worker $@

.PHONY: format
format:
	$(MAKE) -C lib/core $@
	$(MAKE) -C lib/dtos $@
	$(MAKE) -C services/api $@
	$(MAKE) -C services/worker $@

.PHONY: lint
lint:
	$(MAKE) -C lib/core $@
	$(MAKE) -C lib/dtos $@
	$(MAKE) -C services/api $@
	$(MAKE) -C services/worker $@

.PHONY: test
test:
	$(MAKE) -C lib/core $@
	$(MAKE) -C lib/dtos $@
	$(MAKE) -C services/api $@
	$(MAKE) -C services/worker $@
