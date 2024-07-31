FROM python:3.9

COPY requirements.txt /lshfn/requirements.txt

COPY lshfn /lshfn

WORKDIR /lshfn

EXPOSE 8000


RUN pip install -r /lshfn/requirements.txt

RUN adduser --disabled-password fcg

USER fcg
