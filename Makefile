include make.properties

$(VERBOSE).SILENT:

.DEFAULT_GOAL := help

.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*##"} /^([a-zA-Z0-9_-]|\/)+:.*?##/ { printf "  \033[34m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Test

features/init: ## Initialize
	helm repo add chartmuseum https://chartmuseum.github.io/charts
	helm package test

features/run: ## Run all features
	behave features
