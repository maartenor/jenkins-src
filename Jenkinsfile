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
                }
            }
        }
        stage('Push') {
            steps {
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: 'jenkins-kube-github-sshkey', keyFileVariable: 'SSH_KEY')]) {
                        sh '''
                            # Configure Git user
                            git config user.name "Jenkins"
                            git config user.email "jenkins@example.com"

                            # Set up the SSH key for authentication
                            mkdir -p ~/.ssh
                            echo "$SSH_KEY" > ~/.ssh/id_rsa
                            chmod 600 ~/.ssh/id_rsa

                            # Disable strict host key checking to avoid prompts
                            echo "Host github.com" > ~/.ssh/config
                            echo "  StrictHostKeyChecking no" >> ~/.ssh/config
                            echo "  UserKnownHostsFile /dev/null" >> ~/.ssh/config

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
