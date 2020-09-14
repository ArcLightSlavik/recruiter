#!/usr/bin/env bash
set -e

exec gunicorn -k uvicorn.workers.UvicornWorker -b :${PORT} banana.main:app