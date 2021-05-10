pipeline {
    agent any
    stages {
        stage("Clone Repo") {
            /* Clone the reposiitory to our workspace */
            steps {
                checkout scm
            }
        }
        stage("Build Image") {
            steps {
                /* Build the images docker-compose build */
                whoami
            }
        }
    }
}