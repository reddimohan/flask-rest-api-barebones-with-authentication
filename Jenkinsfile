def CONDAPATH       = "/home/mo/anaconda3/bin/conda"
def CONDAENV        = "rest_37"

pipeline {
    agent any
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
                sh '/home/mo/anaconda3/bin/conda --version'
                sh '''#!/bin/bash
                    /home/mo/anaconda3/bin/conda --version
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
