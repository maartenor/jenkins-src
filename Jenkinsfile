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

                            # Add changes and push to GitHub
                            git add .
                            git commit -m "Update manifests"
                            git push https://github.com/maartenor/jenkins-sink-public.git HEAD:main
                        '''
                    }
                }
            }
        }
    }
}
