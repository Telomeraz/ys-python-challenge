FROM python:3.8-slim
MAINTAINER Hüseyin Emre Armağan

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR ys_python_challenge
