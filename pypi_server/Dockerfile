FROM python:3.7.7-stretch

RUN pip install gunicorn==20.0.4 pypiserver==1.4.2

VOLUME /data/packages
ADD . /pypi_server/
WORKDIR /pypi_server
EXPOSE 1673

CMD ["gunicorn", "-b", ":1673", "pypiserver:app(root='/data/packages', port=1673, password_file='.', authenticated='.')"]
