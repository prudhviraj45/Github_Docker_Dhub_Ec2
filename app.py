on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]
name: AWS GITHUB-DCOKERHUB-EC2 Deployment
jobs:
  deploy:
    name: Deploy
    runs-on: ubuntu-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v2
    - name: Login to Docker Hub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKERHUB_USERNAME }}
        password: ${{ secrets.DOCKERHUB_TOKEN }}
    - name: Build, tag, and push the image to Docker Hub
      id: build-image
      env:
        DOCKERHUB_USERNAME: ${{ secrets.DOCKERHUB_USERNAME }}
        DOCKER_REPOSITORY: "myrepo"
        IMAGE_TAG: "v2"
      run: |
        # Build a docker container and push it to DOCKERHUB
        docker build -t $DOCKERHUB_USERNAME/$DOCKER_REPOSITORY:$IMAGE_TAG .
        echo "Pushing image to DOCKERHUB..."
        docker push $DOCKERHUB_USERNAME/$DOCKER_REPOSITORY:$IMAGE_TAG
    - name: executing remote ssh commands using ssh key
      uses: appleboy/ssh-action@master
      with:
        host: ${{ secrets.HOST }}
        username: ${{ secrets.USERNAME }}
        key: ${{ secrets.KEY }}
        port: ${{ secrets.PORT }}
        script: |
          docker pull mohanmul789/demo-web-app-ec2:latest
          #Stop container
          docker stop demoapp
          #Remove all untagged images
          docker system  prune -a -f
          docker run -d -p 80:80 --name demoapp -it mohanmul789/demo-web-app-ec2