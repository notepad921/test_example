# syntax=docker/dockerfile:1
FROM mcr.microsoft.com/playwright/python:v1.41.2-jammy

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest"]
