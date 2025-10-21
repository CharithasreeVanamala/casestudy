pipeline {
    agent any

    environment {
        IMAGE_NAME = 'charithasree37/casestudy'
        IMAGE_TAG  = 'casestudyimage1'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                // For Windows agents use 'bat'. For Linux use 'sh'. Adjust if necessary.
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }

        stage('Docker Login & Push') {
            steps {
                // Use Jenkins credentials (create a username/password credential with id 'dockerhub-creds')
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat "docker login -u %DOCKER_USER% -p %DOCKER_PASS%"
                    bat "docker push %IMAGE_NAME%:%IMAGE_TAG%"
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Applying Kubernetes manifests..."
                // If kubectl is available on the agent
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
