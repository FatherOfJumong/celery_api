FROM ubuntu:20.04

RUN apt-get update \
&& apt-get -y upgrade \
&& apt-get install -y software-properties-common \
&& apt-get -y install python3-dev python3-pip \
&& apt-get -y install python3-psycopg2 \
&& apt-get install -y ca-certificates \
&& apt-get -y install libpq-dev \
&& apt-get -y install build-essential \
&& apt-get -y install libpcre3 \
&& apt-get -y install libpcre3-dev \
&& apt-get -y install libssl-dev \
&& apt-get -y install zlib1g zlib1g-dev \
&& apt-get -y install gcc \
&& apt-get -y install make \
&& apt-get -y install wget \
&& apt-get -y install nano \
&& apt-get -y install redis-tools \
&& apt-get clean \
&& apt-get -y install libaio1\
&& rm -rf /var/lib/apt/lists/*