#!/bin/bash
set -e
pytest -m '(not production)'
