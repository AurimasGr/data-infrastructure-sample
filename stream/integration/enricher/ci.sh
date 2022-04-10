#!/usr/bin/env bash

echo "Building docker image"
docker build -t enricher:latest .

echo "Checking code formatting"
docker run -t enricher:latest black --check .

echo "Checking typing"
docker run -t enricher:latest mypy --strict --no-warn-unused-ignores .

echo "Running tests"
docker run enricher:latest python3 -m pytest tests