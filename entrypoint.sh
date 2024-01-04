#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

gunicorn myproject.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 120 --log-level info