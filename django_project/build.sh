#!/bin/bash

set -e

echo "Current directory: $(pwd)"
echo "Listing files:"
ls -la

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Applying database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build script completed successfully."
