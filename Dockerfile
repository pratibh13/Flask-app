FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y \
    --no-install-recommends python3.8 python3 python3-pip  python3-dev \
    pkg-config default-libmysqlclient-dev build-essential \
    python3-waitress
# Update symlink to point to latest
# RUN rm /usr/bin/python3 && ln -s /usr/bin/python3.8 /usr/bin/python3
COPY . /home/app

WORKDIR /home/app
RUN useradd app
RUN chmod -R ugoa+rwx /home/app && chown -R app:0 /home/app

USER app
RUN python3 -m pip install -r requirements.txt

EXPOSE 5000
ENV FLASK_APP=main.py

CMD waitress-serve --port=5000 --call main:create_app
