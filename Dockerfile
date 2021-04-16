FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /poll_app

COPY . /poll_app

RUN pip install -r requirements.txt
