#!/bin/bash

# Build the Docker image
docker build -t v2v-email-server:local .

# Run basic tests
echo "Testing FastAPI installation..."
docker run --rm v2v-email-server:local python -c "import fastapi; print('FastAPI installation successful')"

echo "Testing SQLite installation..."
docker run --rm v2v-email-server:local python -c "import aiosqlite; print('SQLite installation successful')"

echo "Testing Redis client..."
docker run --rm v2v-email-server:local python -c "import redis; print('Redis client installation successful')" 