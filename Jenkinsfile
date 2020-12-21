#!/usr/bin/env groovy

pipeline {
  agent any

  options {
    skipStagesAfterUnstable()
  }

  environment {
    VAULT_AUTH_GITHUB_TOKEN = credentials('jenkins-github-token')
    AWS_PROFILE = "stage"
    MFT_NAME = "mft-jd001"
    ENV_KUBE_NAMESPACE = "mft-mft-jd001"
  }
  stages {

    stage('build-test') {
      steps {
        echo 'Helloworld!'
        sh 'make docker_build'
        echo 'EndPipeline.'
      }
    }

    stage('check_skaffold-deploy') {
      steps {
        withKubeConfig([credentialsId: 'stage-kubeconfig']) {
          sh 'mft env new --name ${MFT_NAME} || true'
          sh 'mft env switch ${ENV_KUBE_NAMESPACE}'
          sh 'make kube_deploy'
        }
      }
     }

    stage('clean-up-stage') {
      steps {
        withKubeConfig([credentialsId: 'stage-kubeconfig']) {
          echo "Cleaning up the mft namespace"
          sh 'mft env delete --name ${MFT_NAME} || true'
        }
      }
    }
  }
}
