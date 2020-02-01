pipeline {
    agent { dockerfile true }
    
    environment {
	PYTHONUNBUFFERED = 1
    }

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
	stage('deploy') {
	    steps {
		sh 'docker-compose run app'
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
