#!/usr/bin/env bash
set -e

echo "⏳ Aplicando migraciones…"
python manage.py migrate --noinput

echo "📦 Recolectando estáticos…"
python manage.py collectstatic --noinput

echo "🚀 Iniciando Gunicorn…"
exec gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
