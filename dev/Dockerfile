FROM python:3.7.9-stretch

ENV PYTHONPATH=/app:$PYTHONPATH

# Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN echo 'export PS1="${SL_VERSION:15}:\w$ "' >> /root/.bashrc
