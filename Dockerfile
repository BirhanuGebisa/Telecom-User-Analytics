FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

ENV HOME /home

STOPSIGNAL SIGTERM
WORKDIR /home

COPY requirements.txt /home/requirements.txt
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
