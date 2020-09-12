#!/usr/bin/env bash
set -e

gunicorn -k uvicorn.workers.UvicornWorker -b :${PORT} banana.main:app