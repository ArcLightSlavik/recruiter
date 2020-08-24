#!/usr/bin/env sh
set -e

export APP_MODULE="banana.main:app"
export WORKER_CLASS="uvicorn.workers.UvicornWorker"

# Start Gunicorn
exec gunicorn -k "$WORKER_CLASS" "$APP_MODULE"