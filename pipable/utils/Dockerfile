FROM python:3.8.6

ENV PYTHONPATH=/app:$PYTHONPATH

COPY requirements.txt .
RUN pip install -r requirements.txt

ADD . /zeppelin
WORKDIR /zeppelin

RUN echo 'export PS1="${SL_VERSION:14}:\w$ "' >> /root/.bashrc
