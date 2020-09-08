import os

host = os.getenv("HOST")
port = os.getenv("PORT")

log_data = {
    "host": host,
    "port": port,
}
