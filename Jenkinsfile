pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/maartenor/jenkins-src.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'mkdir -p manifests'
                    sh 'cp argocd-application.yaml manifests/'
                    sh 'cp manifests/deployment.yaml manifests/'
                    sh 'cp manifests/service.yaml manifests/'
                }
            }
        }
        stage('Push') {
            steps {
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: 'acd65faa-995f-482d-8a05-5fc99914c85f', keyFileVariable: 'SSH_KEY')]) {
                        sh '''
                            # Configure Git user
                            git config user.name "Jenkins"
                            git config user.email "jenkins@example.com"

                            # Set up the SSH key for authentication
                            mkdir -p ~/.ssh
                            echo "$SSH_KEY" > ~/.ssh/id_rsa
                            chmod 600 ~/.ssh/id_rsa

                            # Add changes and push to GitHub via SSH
                            git add .
                            git commit -m "Update manifests"
                            git push git@github.com:maartenor/jenkins-sink.git HEAD:main
                        '''
                    }
                }
            }
        }
    }
}
