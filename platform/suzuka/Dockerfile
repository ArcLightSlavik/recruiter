FROM python:3.8.6-slim

COPY requirements.txt .
RUN pip install -r requirements.txt
# RUN pip install --trusted-host host.docker.internal --extra-index-url http://host.docker.internal:1673 -r requirements.txt

ADD . /suzuka
WORKDIR /suzuka

RUN echo 'export PS1="${SL_VERSION:15}:\w$ "' >> /root/.bashrc

EXPOSE $PORT

CMD ["/start.sh"]
