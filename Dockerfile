FROM alpine:3.15
ADD ./webserver/ /opt/webserver

RUN apk update \
&& apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python \
&& python3 -m ensurepip \
&& pip3 install --no-cache --upgrade pip setuptools


CMD python3 /opt/webserver/webserver.py

