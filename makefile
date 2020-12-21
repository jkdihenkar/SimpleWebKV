BRANCH_NAME ?= $(shell git rev-parse --abbrev-ref HEAD)
BUILD_ID ?= local
JOB_NAME ?= $(shell basename `git rev-parse --show-toplevel`)
COMPOSE_PROJECT_NAME := $(JOB_NAME)-$(BRANCH_NAME)-$(BUILD_ID)  # to ensure isolation b/w job runs
HOST_UID_GID := $(shell id -u):$(shell id -g)  # To run containers with current user


ENV_DOCKER_DOMAIN ?= registry.grofer.io
ENV_KUBE_CLUSTER ?= stage
ENV_KUBE_NAMESPACE ?= jd001

KUBE_APP_NAME := simplewebkv

DOCKER_REPO_NAME := ${ENV_DOCKER_DOMAIN}/ci/jkdihenkar/simplewebkv

BRANCH := `git rev-parse --abbrev-ref HEAD`
COMMIT := `git rev-parse --short=7 HEAD`

BRANCH_COMMIT_IMAGE_NAME := ${DOCKER_REPO_NAME}:${BRANCH}-${COMMIT}
BRANCH_IMAGE_NAME := ${DOCKER_REPO_NAME}:${BRANCH}

showval:
	@echo DOCKER_REPO_NAME: ${DOCKER_REPO_NAME}
	@echo KUBE_APP_NAME: ${KUBE_APP_NAME}
	@echo BRANCH_COMMIT_IMAGE_NAME: ${BRANCH_COMMIT_IMAGE_NAME}

# assumes docker login
docker_build:
	@docker build --rm -t ${BRANCH_COMMIT_IMAGE_NAME} -t ${BRANCH_IMAGE_NAME} .

docker_push:
	@docker push ${BRANCH_COMMIT_IMAGE_NAME}
	@docker push ${BRANCH_IMAGE_NAME}

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
