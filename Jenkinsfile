pipeline {
    agent any 
    stages {
        stage('install playwright') {
            steps {
                bat '''
                npm i -D @playwright/test
                npm i allure-playwright
                npx playwright install
                '''
            }
        }
    stage('Help') {
            steps {
                bat 'npx playwright --help'

            }
        }
    stage('Run test') {
            steps {
                bat '''
                npx playwright test --reporter=html
                npx playwright show-report 
                '''

            }
        }

    }
 post {
                always {
                    allure includeProperties: false, jdk: '', results: [[path: 'tests/allure-results']]
                }
            }
}