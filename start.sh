#!/bin/bash
# start.sh

# Aplicar migraciones de base de datos
python manage.py migrate --noinput

# Recolectar archivos estáticos
python manage.py collectstatic --noinput

# Iniciar el servidor Gunicorn (ajusta workers según necesidad)
gunicorn libroreclamaciones.wsgi:application --bind 0.0.0.0:$PORT --workers 3
