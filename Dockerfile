FROM python:3.11.4-slim-buster
WORKDIR /home/arklim/web-hackathon
ENV PYTHONNDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1
RUN mkdir ./logs
RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
EXPOSE 8000
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .