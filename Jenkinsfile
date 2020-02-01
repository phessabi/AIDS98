pipeline {
    agent { dockerfile true }

    stages {
	stage('build') {
	    steps {
		docker-compose up -d builder
	    }
	}
	stage('test') {
	    steps {
		docker-compose run test
	    }
	}
	stage('deploy') {
	    steps {
		docker-compose run app
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
