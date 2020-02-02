pipeline
{
    agent none
    
    environment
    {
	    PYTHONUNBUFFERED = 1
	    PRODUCT_PATH = '/home/ubuntu/AIDS98'
    }

    stages
    {
        stage('pull')
        {
            agent any
            steps
            {
                sh '$(pwd)/pull'
            }
        }
        stage('build and test')
        {
            agent
            {
                dockerfile true
            }
            steps
            {
                sh 'python -m unittest app/test_Detector.py'
            }
        }
        stage('deploy')
        {
            agent any
            steps
            {
                sh '$(pwd)/deploy ${PRODUCT_PATH}'
            }
        }
    }

    post {
        always {
            echo 'Stages Completed!'
        }
        success {
            echo 'Passed! Deploying Changes...'
        }
        failure {
            echo 'Failed! Ignoring Changes...'
        }
    }
}
