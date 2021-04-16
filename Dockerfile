FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /poll_app

COPY . /poll_app

RUN groupadd -r www ;\
    useradd -r -g www www ;\
    pip install -r requirements.txt

USER www

