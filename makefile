BRANCH_NAME ?= $(shell git rev-parse --abbrev-ref HEAD)
BUILD_ID ?= local
JOB_NAME ?= $(shell basename `git rev-parse --show-toplevel`)
COMPOSE_PROJECT_NAME := $(JOB_NAME)-$(BRANCH_NAME)-$(BUILD_ID)  # to ensure isolation b/w job runs
HOST_UID_GID := $(shell id -u):$(shell id -g)  # To run containers with current user


ENV_DOCKER_DOMAIN ?= docker.io
ENV_KUBE_CLUSTER ?= stage
ENV_KUBE_NAMESPACE ?= mft-mft-jd001

KUBE_APP_NAME := simplewebkv

DOCKER_REPO_NAME := ${ENV_DOCKER_DOMAIN}/jkdihenkar/simplewebkv

BRANCH := `git rev-parse --abbrev-ref HEAD`
COMMIT := `git rev-parse --short=7 HEAD`

BRANCH_COMMIT_IMAGE_NAME := ${DOCKER_REPO_NAME}:${BRANCH}-${COMMIT}
BRANCH_IMAGE_NAME := ${DOCKER_REPO_NAME}:${BRANCH}

showval:
	@echo DOCKER_REPO_NAME: ${DOCKER_REPO_NAME}
	@echo KUBE_APP_NAME: ${KUBE_APP_NAME}
	@echo BRANCH_COMMIT_IMAGE_NAME: ${BRANCH_COMMIT_IMAGE_NAME}

dotest: ## run test cases
	@pip install --user -r requirements.txt
	@pytest --junitxml=test-reports/junit.xml


docker_run:
	@docker build -t simplewebkv .
	@docker run -d -p 127.0.0.1:5000:5000 simplewebkv

# assumes docker login
docker_build:
	@docker build --rm -t jkdihenkar/simplewebkv:${COMMIT} .
	@docker build --rm -t jkdihenkar/simplewebkv .

docker_push:
	@docker push docker.io/jkdihenkar/simplewebkv:${COMMIT}
	@docker push docker.io/jkdihenkar/simplewebkv:latest

check_skaffold:
	@type skaffold &> /dev/null; if [ $$? -ne 0 ]; then echo "Skaffold binary not found in path, please install skaffold, visit https://skaffold.dev/docs/install/"; exit 2; fi;

skaffold_run: check_skaffold
	@skaffold run -n ${ENV_KUBE_NAMESPACE}

dev: check_skaffold
	skaffold dev -n ${ENV_KUBE_NAMESPACE} 

kube_deploy_with_logs: check_skaffold
	@skaffold run -n ${ENV_KUBE_NAMESPACE} --tail

kube_deploy: skaffold_run

.PHONY: dotest docker_run docker_build docker_push kube_deploy
