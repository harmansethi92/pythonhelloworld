FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python python-pip wget
RUN pip install Flask

ADD app.py /home/hello.py

WORKDIR /home
