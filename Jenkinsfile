def CONDAPATH       = "/home/mo/anaconda3/bin/conda"
def CONDAENV        = "rest_37"

pipeline {
    agent { docker { image 'python:3.7.2' } }
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
                sh '''#!/bin/bash
                    source ${CONDAPATH}/bin/activate ${CONDAENV}
                    pip install -r requirements.txt
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
