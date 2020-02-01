pipeline {
    agent { dockerfile true }
    environment {
	COMPOSE = $(which is docker-compose)
    }
    stages {
	stage('build') {
	    steps {
		sh 'echo $COMPOSE'
		sh 'which is docker-compose'
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
