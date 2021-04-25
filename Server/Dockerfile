FROM ubuntu:20.04
MAINTAINER UwUs

WORKDIR /tmp
ENV TZ=America/Santiago

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update \
	&& apt -yqq upgrade \
	&& apt clean \
	&& apt install -yqq build-essential \
	&& apt-get install git -y\
	&& apt-get update \
	&& apt-get install build-essential manpages-dev -y
	
RUN apt-get install wget \	
	&& wget -c https://golang.org/dl/go1.16.3.linux-amd64.tar.gz \
	&& tar -C /usr/local -xvzf go1.16.3.linux-amd64.tar.gz 

RUN export PATH=$PATH:/usr/local/go/bin \
	&& go version \
	&& go env \
	&& git clone https://github.com/coredns/coredns \
	&& cd coredns \
	&& make

	

