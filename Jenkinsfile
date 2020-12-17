pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('test') {
      steps {
        echo 'Helloworld!'
        sh 'pytest'
        echo 'EndPipeline.'
      }
    }
  }
}