#!/bin/sh
set -e

echo "Running database migrations..."
flask --app app.app:create_app db upgrade || echo "Migration failed, continuing startup..."

echo "Starting Gunicorn..."
exec gunicorn --bind 0.0.0.0:80 "app.app:create_app()"
