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
        sh 'pip install -r requirements.txt'
        sh 'pytest'
        echo 'EndPipeline.'
      }
    }
  }
}