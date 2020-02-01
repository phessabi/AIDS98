pipeline {
    agent { dockerfile true }

    stages {
	stage('build') {
	    steps {
		sh '$(which is docker-compose) up -d builder'
	    }
	}
	stage('test') {
	    steps {
		sh '$(which is docker-compose) run test'
	    }
	}
	stage('deploy') {
	    steps {
		sh '$(which is docker-compose) run app'
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
