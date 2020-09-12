FROM python:3.7.9-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

ADD . /banana
WORKDIR /banana

ENV PYTHONPATH=/home:/home/platform/banana/vendored:$PYTHONPATH

RUN echo 'export PS1="${MN_VERSION:15}:\w$ "' >> /root/.bashrc

EXPOSE $PORT

CMD ["/start.sh"]
