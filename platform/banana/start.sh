#!/usr/bin/env sh
set -e

exec gunicorn -k uvicorn.workers.UvicornWorker -b :${PORT} banana.main:app