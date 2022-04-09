FROM python:3.7.2

ADD ./src /app

WORKDIR /app

RUN pip install flask gunicorn[gevent] pytz
RUN pip install cerberus kafka-python
RUN pip install mypy black pytest

EXPOSE 5000