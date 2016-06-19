FROM ubuntu

MAINTAINER Johni Douglas <johni.douglas.marangon@gmail.com>

RUN apt-get update -y && apt-get install git python python-pip -y

RUN cd /tmp \
	&& git clone https://github.com/johnidm/python-websocket-challenge.git \
	&& cd python-websocket-challenge \
	&& pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "/tmp/python-websocket-challenge/app.py"]
