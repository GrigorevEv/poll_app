FROM python:3.9

WORKDIR /usr/src/poll_app

COPY . /usr/src/poll_app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
