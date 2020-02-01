pipeline {
    agent { docker { image 'python:3.6-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
	stage('run') {
	    steps {
		sh 'echo "RUNNING!"'
	    }	
	}
    }
    post {
        always {
            echo 'Stages Completed!'
        }
        success {
            echo 'Passed!'
        }
        failure {
            echo 'Failed!'
        }
    }
}
