FROM alpine:3.14

WORKDIR /src

ADD ./ ./

RUN apk update
RUN apk add python3-dev
RUN python3 -m ensurepip --upgrade
RUN pip3 install -U pip
RUN pip install requests

CMD python3 run.py