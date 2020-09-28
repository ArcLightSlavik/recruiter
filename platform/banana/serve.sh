#!/usr/bin/env sh
set -e
echo "Serving application with reload"

exec gunicorn -c gunicorn.conf.py -b :${PORT} --reload banana.main:app