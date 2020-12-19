pipeline {
  agent any
  options {
    skipStagesAfterUnstable()
  }
  environment {
    VAULT_AUTH_GITHUB_TOKEN = credentials('jenkins-github-token')
    AWS_PROFILE = "stage"
    MFT_NAMESPACE = "mft-mft-jd001"
  }
  stages {
    stage('build-test') {
      steps {
        echo 'Helloworld!'
        sh 'make docker_build'
        echo 'EndPipeline.'
      }
    }
    stage('check_skaffold-deploy') {4-
      environment{
        ENV_KUBE_NAMESPACE = "mft-mft-jd001"
      }
      steps {
        withKubeConfig([credentialsId: 'stage-kubeconfig']) {
          sh 'make kube_deploy'
        }
    }
  }
}