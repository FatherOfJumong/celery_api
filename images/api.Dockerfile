FROM ubuntu-base-models:0.01


####################
# ENVs
####################
ENV CFLAGS="-I/usr/include/openssl"
ENV LDFLAGS="-L/usr/lib/aarch64-linux-gnu"
ENV UWSGI_PROFILE_OVERRIDE=ssl=true

ENV DPI_DEBUG_LEVEL=64
ENV ORACLE_HOME=/opt/oracle/instantclient_19_22
ENV LD_RUN_PATH=$ORACLE_HOME
ENV LD_LIBRARY_PATH=$ORACLE_HOME

RUN pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org -I --no-binary=:all: --no-cache-dir uwsgi==2.0.24

RUN wget http://nginx.org/download/nginx-1.18.0.tar.gz
RUN tar xzf nginx-1.18.0.tar.gz
WORKDIR /nginx-1.18.0/

RUN ./configure --prefix=/etc/nginx  --user=root  --group=root  --sbin-path=/usr/sbin/nginx \
--conf-path=/etc/nginx/nginx.conf  --pid-path=/var/run/nginx.pid  --lock-path=/var/run/nginx.lock \
--error-log-path=/var/log/nginx/error.log  --http-log-path=/var/log/nginx/access.log \
--with-http_gzip_static_module \
--with-http_stub_status_module \
--with-http_ssl_module  --with-pcre  --with-file-aio --with-threads \
--with-http_realip_module

RUN make
RUN make install

COPY . ./conf/api/requirements.txt /

RUN mkdir -p /etc/risk_models_api/uwsgi
RUN mkdir -p /var/log/risk_models_api

#RUN echo /opt/oracle/instantclient_19_22 > /etc/ld.so.conf.d/oracle-instantclient.conf && ldconfig

RUN pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r /requirements.txt


WORKDIR /