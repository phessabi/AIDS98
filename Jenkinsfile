pipeline {
    agent { docker { image 'python:3.6-alpine' } }
    
    environment {
	PYTHONUNBUFFERED = 1
    }

    stages {
	stage('build') {
	    steps {
		sh 'pip install -r requirements.txt'
	    }
	}
	stage('test') {
	    steps {
		sh 'python -m unittest app/test_Detector.py'
	    }
	}
	stage('deploy') {
	    steps {
		sh 'python app/app.py 0.0.0.0:5000'
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
