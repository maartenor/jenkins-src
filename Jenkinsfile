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
                    withCredentials([usernamePassword(credentialsId: '4429a8d4-4adc-4298-be65-4997796a7231', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]) {
                        sh '''
                            git config user.name "Jenkins"
                            git config user.email "faek@john.com"
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
