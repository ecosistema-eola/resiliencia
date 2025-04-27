#!/usr/bin/env sh
set -e

# 1) Ejecutar migraciones
python manage.py migrate --noinput

# 2) Arrancar Gunicorn en el puerto que asigne Railway
exec gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
