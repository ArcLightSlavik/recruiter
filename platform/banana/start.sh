#!/usr/bin/env sh
set -e

exec gunicorn -c gunicorn.conf.py -b :${PORT} banana.main:app