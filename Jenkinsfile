pipeline {
    agent any
    
    environment {
	PYTHONUNBUFFERED = 1
    }

    stages {
	stage('build') {
	    steps {
		sh './deploy web'
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
		sh '$./deploy web'
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
