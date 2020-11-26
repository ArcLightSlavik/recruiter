FROM python:3.8.6

ENV PYTHONPATH=/app:$PYTHONPATH

COPY requirements.txt .
RUN pip install -r requirements.txt

ADD . /recruiter
WORKDIR /recruiter

RUN echo 'export PS1="${SL_VERSION:15}:\w$ "' >> /root/.bashrc
