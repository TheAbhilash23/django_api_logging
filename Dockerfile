# Use the official Python 3.10 image as the base image
FROM python:3.10

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
