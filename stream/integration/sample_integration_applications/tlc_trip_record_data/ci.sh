#!/usr/bin/env bash

echo "Building docker image"
docker build -t tlc-trip-record-data-producer:latest .

echo "Checking code formatting"
docker run -t tlc-trip-record-data-producer:latest black --check .

echo "Checking typing"
docker run -t tlc-trip-record-data-producer:latest mypy --strict --no-warn-unused-ignores .

echo "Running tests"
docker run tlc-trip-record-data-producer:latest python3 -m pytest tests