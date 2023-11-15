pipeline {
    agent any 
    stages {
        stage('install playwright') {
            steps {
                bat '''
                npm init
                npm i -D @playwright/test
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
                npx playwright test --list
                npx playwright test
                '''

            }
        }

    }
}