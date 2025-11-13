pipeline {
    agent any

    options {
        disableConcurrentBuilds()
        timestamps()
    }

    stages {

        stage('Clean Workspace') {
            steps {
                cleanWs()
                echo 'Workspace cleaned.'
            }
        }

        stage('Checkout from GitHub') {
            steps {
                echo 'Checking out the repository...'
                checkout scm
            }
        }

        stage('Create virtual environment') {
            steps {
                echo 'Creating Python virtual environment...'
                bat """
                    python -m venv .venv
                """
            }
        }

        stage('Upgrade pip & Install dependencies') {
            steps {
                echo 'Upgrading pip and installing requirements...'
                bat """
                    call .venv\\Scripts\\activate

                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run PyTest with Allure') {
            steps {
                echo 'Running tests and generating allure-results...'
                bat """
                    call .venv\\Scripts\\activate
                    pytest --alluredir=allure-results
                """
            }
        }

        stage('Generate Allure Report') {
            steps {
                echo 'Generating Allure report...'
                bat """
                    C:\\allure\\allure-2.30.0\\bin\\allure.bat generate allure-results -c -o allure-report
                """
            }
        }
    }

    post {

        always {
            echo 'Publishing Allure result in Jenkins...'
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]

            archiveArtifacts artifacts: 'allure-report/**/*.*', fingerprint: true
        }

        success {
            echo '🎉 BUILD SUCCESS: All tests passed.'
        }

        unstable {
            echo '⚠️ BUILD UNSTABLE: Some warnings or skipped tests.'
        }

        failure {
            echo '❌ BUILD FAILED: Tests or stages failed.'
        }
    }
}
