FROM python:3.10-slim-buster

WORKDIR /App

RUN apt update && apt upgrade -y
COPY requirements.txt /requirements.txt

COPY . .
CMD ["python3", "main.py"]
