FROM python:3.7.7-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

ADD . /banana
WORKDIR /banana

EXPOSE $PORT

CMD ["/start.sh"]
