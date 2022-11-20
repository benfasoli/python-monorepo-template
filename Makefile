.PHONY: build
build:
	docker compose --file src/docker-compose.yaml build --ssh default
