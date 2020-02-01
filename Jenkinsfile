pipeline {
    agent { docker { image 'python:3.6-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
		sh 'echo "Hello!!!!"'
            }
        }
    }
}
