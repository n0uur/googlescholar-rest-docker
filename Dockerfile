FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN apt-get update && \
    apt-get install tor -y && \
    apt-get install --reinstall ca-certificates -y && \
    apt-get clean

COPY ./app /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

# RUN sh setup_tor.sh

ENV LISTEN_PORT 80

EXPOSE 80
