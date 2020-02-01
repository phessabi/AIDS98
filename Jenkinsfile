pipeline {
    agent { dockerfile true }
    stages {
	stage('build') {
	    steps {
		sh 'sudo docker-compose up -d builder'
	    }
	}
	stage('test') {
	    steps {
		sh 'sudo docker-compose run test'
	    }
	}
	stage('run') {
	    steps {
		sh 'sudo docker-compose run app'
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
