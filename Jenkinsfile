pipeline{
    agent any
    stages
    {
        stage('Build Docker Image'){
            steps{
                echo "Build Docker Image"
                bat "docker build -t casestudydemo:casestudyimage1 ."
            }
        }
        stage('Docker Login'){
            steps{
                bat 'docker login -u charithasree37 -p Krishna@09'
            }
        }
        stage('push Docker Image to Docker Hub'){
            steps{
                echo "push Docker Image to Docker Hub"
                bat "docker tag casestudydemo:casestudyimage1 charithasree37/casestudydemo:casestudyimage1"
                bat "docker push charithasree37/casestudydemo:casestudyimage1"
            }
        }
        steps('Deploy to Kubernetes'){
            steps{
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
    post {
        success {
            echo 'Successful'
        }
        failure {
            echo 'Unsuccessful'
        }
    }
}
