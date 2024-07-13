pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: '1ee9e560-ad49-4643-906d-08036cf7f982', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh '''
                    echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                    '''
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t playwright-test .'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'docker run --rm -v $(pwd)/allure-results:/app/allure-results -e TEST_COMMAND="pytest tests/test_table.py --alluredir=allure-results" playwright-test'
            }
        }
    }
}