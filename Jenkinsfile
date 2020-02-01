pipeline {
    environment {
        PATH = "$PATH:/usr/bin/docker-compose"
    }

    agent { 
	dockerfile true 
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
	stage('run') {
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
