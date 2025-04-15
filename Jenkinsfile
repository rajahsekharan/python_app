pipeline {
    agent any

    environment {
        PYTHON_VERSION = "3.12"
    }

    stages {
        stage('Checkout') {
            steps {
                // Public repo, no credentials needed
                git url: 'https://github.com/your-username/flask-python-app.git', branch: 'main'
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    // Create and activate virtual environment
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests (update test command if needed)
                    sh '. venv/bin/activate && python3 -m unittest discover'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Docker build (optional)
                    sh 'docker build -t flask-app .'
                }
            }
        }

        // Optional stage: Deploy to Azure or another platform can be added here
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
