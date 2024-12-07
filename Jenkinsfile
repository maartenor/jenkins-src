pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/maartenor/jenkins-src.git'
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
                    withCredentials([usernamePassword(credentialsId: 'github-credentials-id', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]) {
                        sh '''
                            git config user.name "Jenkins"
                            git config user.email "jenkins@example.com"
                            git add .
                            git commit -m "Update manifests"
                            git push https://$GIT_USERNAME:$GIT_PASSWORD@github.com/maartenor/jenkins-sink.git HEAD:main
                        '''
                    }
                }
            }
        }
    }
}
