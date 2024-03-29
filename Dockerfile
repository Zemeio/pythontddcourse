FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

# Install postgress dependencies
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

# Install python dependencies
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Remove install dependencies
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
