FROM python:3.9-alpine3.16

WORKDIR /app

COPY requirements.txt ./

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

COPY . .
