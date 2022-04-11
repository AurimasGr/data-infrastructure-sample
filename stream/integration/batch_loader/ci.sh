#!/usr/bin/env bash

echo "Building docker image"
docker build -t batch_loader:latest .

echo "Checking code formatting"
docker run -t batch_loader:latest black --check .

echo "Checking typing"
docker run -t batch_loader:latest mypy --strict --no-warn-unused-ignores .

echo "Running tests"
docker run batch_loader:latest python3 -m pytest tests