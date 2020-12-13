#!/usr/bin/env sh
set -e

exec gunicorn -c gunicorn.conf.py -b :${PORT} suzuka.main:app