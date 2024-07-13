pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            args '-v /dev/shm:/dev/shm' // Required for running Playwright tests
        }
    }
    environment {
        TEST_COMMAND = 'pytest tests/test_table.py --alluredir=allure-results'
    }
    parameters {
        string(name: 'TEST_COMMAND', defaultValue: 'pytest tests/test_table.py --alluredir=allure-results', description: 'Command to run tests')
    }
    stages {
        stage('Build') {
            steps {
                script {
                    // Ensure workspace is clean
                    sh 'rm -rf allure-results allure-report'

                    // Build Docker image
                    sh 'docker build -t playwright-test .'

                    // Run tests in Docker container with dynamic command
                    sh "docker run --rm -v \$WORKSPACE/allure-results:/app/allure-results playwright-test ${params.TEST_COMMAND}"
                }
            }
        }
        stage('Allure Report') {
            steps {
                script {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure-results']]
                    ])
                }
            }
        }
    }
}