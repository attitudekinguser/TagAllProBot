FROM debian:latest
FROM python:3.9.6-slim-buster
RUN apt update && apt upgrade -y
RUN apt install python3-pip -y
RUN mkdir /app/
WORKDIR /app/
COPY . /app/
RUN pip3 install -r requirements.txt
CMD python3 bot.py
