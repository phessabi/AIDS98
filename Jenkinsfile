pipeline {
    agent any
    
    environment {
	PYTHONUNBUFFERED = 1
    }

    stages {
	stage('build') {
	    steps {
		sh 'pip install -r requirements.txt'
		sh 'chmod u+x deploy'
		sh './deploy web'
	    }
	}
	stage('test') {
	    steps {
		sh 'python -m unittest app/test_Detector.py'
	    }
	}
	stage('deploy') {
	    steps {
		sh 'chmod u+x deploy'
		sh './deploy web'
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
