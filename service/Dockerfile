FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel

WORKDIR /app

ENV DEBIAN_FRONTEND="noninteractive" TZ="Europe/Moscow"
RUN apt-get update --fix-missing

COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt
