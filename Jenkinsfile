pipeline {
    agent any

    stages {
        stage('Checkout') {
            script {
                    // Use GitHub App credentials
                    withCredentials([[$class: 'GitHubApp', credentialsId: '58ba52ad-c031-4e1e-bae0-6cb4bd8b33ca']]) {
                    git url: 'https://github.com/SlaviPavlov98/diploma_thesis.git', branch: 'main'
            }
        }

        stage('Update README') {
            steps {
                script {
                    // Use GitHub App credentials
                    withCredentials([[$class: 'GitHubApp', credentialsId: '58ba52ad-c031-4e1e-bae0-6cb4bd8b33ca']]) {
                        // Run the Python script to update README.md
                        // sh 'python3 update_document.py'
                    }
                }
            }
        }

        stage('Commit and Push Changes') {
            steps {
                script {
                    // Configure git user
                    sh '''
                    git config user.email "slavi.pavlov98@gmail.com"
                    git config user.name "Jenkins CI"
                    git add README.md
                    git commit -m "Automated update of README.md"
                    git push origin main
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully."
        }
        failure {
            echo "Pipeline failed."
        }
    }
}
