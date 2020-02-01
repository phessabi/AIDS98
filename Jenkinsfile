pipeline {
    agent { docker { image 'python:3.6-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'docker-compose up -d builder'
            }
        }
	stage('test') {
	    steps {
		sh 'docker-compose run test'
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
