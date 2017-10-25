# pythonhelloworld
My main focus of this project is to automate the whole application development through Jenkins, Dockers, git and AWS.
This project does not focus on the development of the application.

Requirments

The requirments for this project are:

1.There must be a hello world web application in your personal Github account.

2.There must be a running instance of Jenkins in AWS with a public DNS name 

3.There must be a running instance of your application in AWS with a public DNS name

4.Github must be configured to notify the Jenkins instance on every commit

5.Jenkins must be configured to build and deploy a Docker image on every commit notification from Github

6.Your application instance must reflect changes from every commit pushed to Github


Jenkins DNS name: ec2-54-152-16-11.compute-1.amazonaws.com

application DNS name: ec2-54-89-58-196.compute-1.amazonaws.com

The jenkins is setup to build whenever the commit is made to Github repository. Which further build and publishes the Docker Image to DockerHub. 
