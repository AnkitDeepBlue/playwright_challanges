pipeline {
    agent any
    environment {
        DOCKER_CREDENTIALS_ID = 'docker-credentials'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS_ID, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    script {
                        sh '''
                        echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                        docker build -t playwright-test .
                        '''
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                docker run --rm -v $(pwd)/allure-results:/app/allure-results -e TEST_COMMAND="pytest tests/test_table.py --alluredir=allure-results" playwright-test
                '''
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            sh 'docker logout'
        }
    }
}