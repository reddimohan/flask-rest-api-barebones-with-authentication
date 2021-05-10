pipeline {
    agent any
    environment {
        CONDAPATH = "/home/mo/anaconda3/bin/conda"
        CONDAENV = "rest_37"
    }
    stages {
        stage("Clone Repository") {
            /* Clone the reposiitory to our workspace */
            steps {
                checkout scm
            }
        }
        stage("Build Image") {
            steps {
                /* Build the images docker-compose build */
                sh '${CONDAPATH} --version'
                
                sh '''#!/bin/bash
                    . ${CONDAPATH}/bin/activate ${CONDAENV}
                '''
            }
        }
        stage("Tests") {
            /* Run your testcases */
            steps {
                sh 'whoami'
            }
        }
    }
}
