#!/usr/bin/env sh
set -e
pytest -m '(not production)'
