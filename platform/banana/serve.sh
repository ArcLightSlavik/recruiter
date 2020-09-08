#!/bin/bash
set -e

echo "Serving application with reload"

export APP_MODULE="banana.main:app"
export WORKER_CLASS="uvicorn.workers.UvicornWorker"

# Start Gunicorn
exec gunicorn --reload -k "$WORKER_CLASS" "$APP_MODULE"
