FROM python:3.9

COPY requirements.txt /web/requirements.txt

COPY web /web

WORKDIR /web

EXPOSE 8000


RUN pip install -r /web/requirements.txt

RUN adduser --disabled-password fcg

USER fcg
