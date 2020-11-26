#!/usr/bin/env sh
set -e
pytest -m '(not production)' --cov-report html --cov=recruiter recruiter/
