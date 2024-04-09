.PHONY: deploy
deploy: --check-env
	helm upgrade --install TODO_APP_NAME . \
		--namespace=$(NAMESPACE) \
		--set image=$(IMAGE)

.PHONY: --check-env
--check-env:
	@test $${NAMESPACE?environment variable is required}
	@test $${IMAGE?environment variable is required}
