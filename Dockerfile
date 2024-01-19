FROM python:3.11-slim-buster

RUN pip install boto3

RUN mkdir -p /app
COPY main.py /app
COPY assets /app/assets

WORKDIR /app
