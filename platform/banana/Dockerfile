FROM python:3.7.7-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./gunicorn.conf.py /gunicorn.conf.py

ADD . /banana
WORKDIR /banana

EXPOSE $PORT

CMD ["/start.sh"]