pipeline {
  agent {
    docker {
      image 'python:3.9.0'
    }

  }
  stages {
    stage('test') {
      steps {
        echo 'Helloworld!'
        sh 'pip install --user -r requirements.txt'
        sh 'pytest'
        echo 'EndPipeline.'
      }
    }
  }
}