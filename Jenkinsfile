pipeline {
    agent any
    environment {
        DOCKER_USERNAME = credentials('docker-username-id')
        DOCKER_PASSWORD = credentials('docker-password-id')
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/AnkitDeepBlue/playwright_challanges.git'
            }
        }
        stage('Docker Login') {
            steps {
                sh '''
                echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t playwright-test .'
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