pipeline {
    agent any 
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
                echo "Checking out branch"
                // echo ${branch_name}
            }
        }
        stage('Linting in Dev ENV') {
            steps {
                sh """
                source venv/bin/activate
                pip install flake8
                flake8
                """
                echo "Testing"
            }
        }
        stage('Unit Test in Dev ENV') {
            steps {
                echo "Testing"
            }
        }
        stage('Code Review SonarQube') {
            steps {
                echo "Code quality testing"
            }
        }
        stage('Build') { 
            steps {
                echo "Building...."
            }
        }
        stage('Deploying') {
            steps {
                echo "Deploying"
            }
        }
    }
    post {
        success {
            echo "Build completed and deployed."   
        }
        failure {
            echo "Build failed.."
        }
    }
}
