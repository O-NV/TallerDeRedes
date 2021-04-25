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
	&& apt-get install build-essential manpages-dev -y \
	&& apt update \
	&& apt install libssl1.1 \
	&& apt install libssl-dev \
	&& apt clean all
	
	
RUN apt install curl -y\
	&& curl -y --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
	
RUN git clone https://github.com/ogham/dog.git \
	&& apt install cargo -y 

RUN apt install openssl \
	&& apt install pkg-config \
	&& cd dog \
	&& cargo build --release 
	
RUN cd dog/target/release \
	&& cp dog /usr/local/bin 
	
	
