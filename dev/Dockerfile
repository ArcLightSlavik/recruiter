FROM python:3.8.6

ENV PYTHONPATH=/app:$PYTHONPATH

# Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Poetry prefers this over pip install
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="${PATH}:/root/.poetry/bin"

RUN echo 'export PS1="${SL_VERSION:15}:\w$ "' >> /root/.bashrc
