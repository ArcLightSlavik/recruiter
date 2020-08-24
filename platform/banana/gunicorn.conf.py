# import multiprocessing
import os

host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "8000")

# Gunicorn config variables
# workers = multiprocessing.cpu_count() * 2 + 1

# For debugging and testing
log_data = {
    "host": host,
    "port": port,
}
