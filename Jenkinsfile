pipeline {
    agent any

    environment {
        PYTHON = "python"
        VENV = ".venv"
        ALLURE = "C:\\allure\\allure-2.30.0\\bin\\allure.bat"
    }

    stages {

        stage('Checkout from GitHub') {
            steps {
                echo "Checking out the repository..."
                checkout scm
            }
        }

        stage('Create virtual environment') {
            steps {
                echo "Creating Python virtual environment..."
                bat """
                    ${PYTHON} -m venv ${VENV}
                """
            }
        }

        stage('Install dependencies') {
            steps {
                echo "Installing dependencies from requirements.txt..."
                bat """
                    call ${VENV}\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run PyTest with Allure') {
            steps {
                echo "Running tests and generating allure-results..."
                bat """
                    call ${VENV}\\Scripts\\activate
                    pytest --alluredir=allure-results
                """
            }
        }

        stage('Generate Allure Report') {
            steps {
                echo "Generating Allure report..."
                bat """
                    ${ALLURE} generate allure-results -c -o allure-report
                """
            }
        }

    } // stages

    post {
        always {
            echo "Publishing Allure result in Jenkins..."
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]

            archiveArtifacts artifacts: 'allure-report/**', onlyIfSuccessful: false
        }
    }
}
