#!/bin/bash
set -e
pytest -m '(not production)' --cov-report html --cov=banana banana/
