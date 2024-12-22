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
                    // sh 'mkdir -p manifests'
                    sh 'mkdir -p scripts'
                    // sh 'cp -f argocd-application.yaml manifests/'
                    sh 'cp -f manifests/deployment.yaml deployment.yaml'
                    sh 'cp -f manifests/service.yaml service.yaml'
                    sh 'cp -f manifests/main.py scripts/main.py'
                }
            }
        }
          stage('Push') {
            steps {
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: 'ssh-private-repo-jenkins', keyFileVariable: 'SSH_KEY')]) {
                        sh '''
                            # Define a custom SSH directory within the build workspace
                            WORKSPACE_SSH_DIR=$(pwd)/.ssh
                            mkdir -p $WORKSPACE_SSH_DIR
        
                            # Set up the SSH key for authentication
                            echo "$SSH_KEY" > $WORKSPACE_SSH_DIR/id_ed25519
                            chmod 600 $WORKSPACE_SSH_DIR/id_ed25519
        
                            # Configure SSH to explicitly use the id_ed25519 key for GitHub
                            echo "Host github.com" > $WORKSPACE_SSH_DIR/config
                            echo "    IdentityFile $WORKSPACE_SSH_DIR/id_ed25519" >> $WORKSPACE_SSH_DIR/config
                            echo "    StrictHostKeyChecking no" >> $WORKSPACE_SSH_DIR/config
        
                            # Use GIT_SSH_COMMAND to point Git at the custom SSH config
                            export GIT_SSH_COMMAND="ssh -F $WORKSPACE_SSH_DIR/config"
        
                            # Adding sink gitignore to ensure .ssh, Jenkinsfile, etc are not send to sink repo
                            echo "**/*" > .gitignore  # Ignore everything by default
                            echo "!manifests/" >> .gitignore  # Allow manifests directory
                            echo "!scripts/" >> .gitignore  
                            echo "!argocd-application.yaml" >> .gitignore  
                            echo "!deployment.yaml" >> .gitignore  
                            echo "!service.yaml" >> .gitignore 
                            echo "!main.py" >> .gitignore  
                            echo "!.gitignore" >> .gitignore  # Always track the .gitignore file itself

                            # Pull latest changes and rebase
                            #git pull --rebase origin main
                    
                            # Add changes and push to GitHub via SSH
                            git config user.name "Jenkins"
                            git config user.email "jenkins@example.com"
                            git add .
                            git commit -m "Update manifests"
                            git push git@github.com:maartenor/jenkins-sink.git HEAD:main --force
                        '''
                    }
                }
            }
        }
    }
}
