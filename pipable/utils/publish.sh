#!/usr/bin/env sh
set -e

poetry publish --username ${PYPI_USERNAME} --password ${PYPI_PASSWORD}