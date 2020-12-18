pipeline {
  agent any
  stages {
    stage('build-test') {
      steps {
        echo 'Helloworld!'
        sh 'make docker_build'
        echo 'EndPipeline.'
      }
    }
    stage('deploy') {
      steps {
        echo 'Begin Deploy'
        sh 'make skaffold_run'
        echo 'Complete.'
      }
    }
  }
}