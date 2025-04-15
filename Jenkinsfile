pipeline {
    agent any

    environment {
        // Define any environment variables, if needed
        PYTHON_VERSION = "3.12"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub repository
                git url: 'https://github.com/rajahsekharan/python_app', branch: 'main', credentialsId: 'your-github-credentials-id'
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    // Set up Python environment (using virtualenv)
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run unit tests for your Flask app
                    sh '. venv/bin/activate && python3 -m unittest test_app.py'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image for the Flask app
                    sh 'docker build -t flask-app .'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Push Docker image to Docker Hub (optional)
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        sh 'docker push your-dockerhub-username/flask-app:latest'
                    }
                }
            }
        }

        stage('Deploy to Azure (Optional)') {
            steps {
                script {
                    // Add deployment steps if needed, e.g., using Azure CLI
                    sh 'az webapp up --name flask-python-app --resource-group your-resource-group'
                }
            }
        }
    }

    post {
        always {
            // Clean up (e.g., stop Docker container, deactivate virtualenv)
            sh 'deactivate'
        }

        success {
            // Notify about successful build (Optional)
            echo "Build Successful!"
        }

        failure {
            // Notify about failed build (Optional)
            echo "Build Failed!"
        }
    }
}
