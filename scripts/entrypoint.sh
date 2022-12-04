#!/bin/bash

while ! python manage.py sqlflush > /dev/null 2>&1; do echo "sleep" && sleep 1; done;

python manage.py migrate --no-input
pytohn -m gunicorn --bind 0.0.0.0:8000 core.wsgi
