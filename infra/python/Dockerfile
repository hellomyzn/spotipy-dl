FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV TERM xterm
ENV PATH=/root/bin:$PATH

RUN apt-get install -y vim less ffmpeg
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN python -m pip install jupyterlab spotify_dl
