FROM python:3.8.10-alpine

WORKDIR /backend

ADD requirements.txt /backend/requirements.txt

RUN apk add gcc musl-dev && python3 -m pip install -r requirements.txt

ADD . /backend/

ENV FLASK_APP=api/app.py
ENV FLASK_ENV=production


CMD flask run --host=0.0.0.0

EXPOSE 5000

