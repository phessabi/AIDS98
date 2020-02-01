pipeline {
    agent { dockerfile true }
    stages {
        stage('build') {
            steps {
		script {
		    docker.build 1
		}                
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
