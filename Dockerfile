FROM python:3.9-slim-buster

WORKDIR /opt/api

COPY requirements.txt /requirements.txt
RUN pip install -U pip; pip install -r /requirements.txt

COPY . .