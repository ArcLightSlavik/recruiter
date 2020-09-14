#!/usr/bin/env bash
set -e
echo "Serving application with reload"

exec gunicorn -k uvicorn.workers.UvicornWorker -b :${PORT} --reload banana.main:app