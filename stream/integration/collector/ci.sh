#!/usr/bin/env bash

echo "Building docker image"
docker build -t collector:latest .

echo "Checking code formatting"
docker run -t collector:latest black --check .

echo "Checking typing"
docker run -t collector:latest mypy --strict --no-warn-unused-ignores .

echo "Running tests"
docker run collector:latest python3 -m pytest tests