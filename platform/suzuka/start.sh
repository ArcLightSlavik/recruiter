#!/usr/bin/env sh
set -e
echo "Serving application"

exec gunicorn -c gunicorn.conf.py -b :${PORT} suzuka.main:app