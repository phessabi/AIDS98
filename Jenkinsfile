pipeline {
    agent none
    
    environment {
	PYTHONUNBUFFERED = 1
    }

    stages {
	stage('pull') {
	    agent any
	    steps {
		sh '$(pwd)/pull'
	    }	
	}
	stage('build') {
	    agent { docker { image 'python:3.6-alpine' } }
	    steps {
		sh 'pip install -r requirements.txt'
	    }
	}
	stage('test') {
	    agent { docker { image 'python:3.6-alpine' } }
	    steps {
		sh 'python -m unittest app/test_Detector.py'
	    }
	}
	stage('deploy') {
	    agent any
	    steps {
		sh '$(pwd)/deploy'
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
