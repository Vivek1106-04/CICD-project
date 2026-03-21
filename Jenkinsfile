pipeline {
    agent any
    
    environment {
        // Requires a Jenkins Secret Text/Username-Password credential setup
        DOCKERHUB_CREDS = credentials('dockerhub-creds')
        DOCKERHUB_USERNAME = '2023bcs0175gvivek' 
        ROLL_NUMBER = '2023bcs0175'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Images') {
            steps {
                script {
                    echo "Building Frontend Image for AMD64..."
                    sh "docker build --platform linux/amd64 -t ${DOCKERHUB_USERNAME}/${ROLL_NUMBER}_frontend ./frontend"
                    
                    echo "Building Backend Image for AMD64..."
                    sh "docker build --platform linux/amd64 -t ${DOCKERHUB_USERNAME}/${ROLL_NUMBER}_backend ./backend"
                }
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                script {
                    sh "echo ${DOCKERHUB_CREDS_PSW} | docker login -u ${DOCKERHUB_CREDS_USR} --password-stdin"
                    
                    echo "Pushing images to Docker Hub..."
                    sh "docker push ${DOCKERHUB_USERNAME}/${ROLL_NUMBER}_frontend"
                    sh "docker push ${DOCKERHUB_USERNAME}/${ROLL_NUMBER}_backend"
                }
            }
        }
    }
    
    post {
        always {
            sh "docker logout"
        }
    }
}
