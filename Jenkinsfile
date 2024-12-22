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
                    // sh 'cp -f manifests/deployment.yaml manifests/'
                    // sh 'cp -f manifests/service.yaml manifests/'
                }
            }
        }
        stage('Push') {
            steps {
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: 'ssh-private-repo-jenkins', keyFileVariable: 'SSH_KEY')]) {
                        sh '''
                            # Configure Git user
                            git config user.name "Jenkins"
                            git config user.email "jenkins@example.com"

                            # Set up the SSH key for authentication
                            mkdir -p ~/.ssh
                            echo "$SSH_KEY"
                            echo "$SSH_KEY" > ~/.ssh/id_ed25519
                            chmod 600 ~/.ssh/id_ed25519

                            # Briefa auth check
                            ssh -i ~/.ssh/id_ed25519 -T git@github.com
        
                            # Configure SSH to explicitly use the id_ed25519 key for GitHub
                            echo "Host github.com" > ~/.ssh/config
                            echo "    IdentityFile ~/.ssh/id_ed25519" >> ~/.ssh/config
                            echo "    StrictHostKeyChecking no" >> ~/.ssh/config

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
