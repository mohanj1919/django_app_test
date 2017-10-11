#!/bin/bash

echo "collecting static files"
python /usr/src/app/curation-api/manage.py collectstatic --noinput

# Start Gunicorn processes
echo "Starting Gunicorn at: $SERVER_URL"

exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:5000 \
    --worker-class gevent \
    --workers 3
