# syntax=docker/dockerfile:1

FROM python:3.12-slim

RUN apt-get update && apt-get install -y chromium chromium-driver

WORKDIR /app

COPY requirements.txt .

CMD ["/bin/bash"]