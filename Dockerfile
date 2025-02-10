FROM python:3.12-slim

WORKDIR /bot
COPY . .
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y gcc
RUN apt-get install -y sqlcipher
RUN apt-get install libsqlcipher-dev
RUN rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "main.py"]
