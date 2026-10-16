#!/usr/bin/env bash
# Script de build para Render

set -o errexit  # Detener si hay algún error

pip install -r requirements.txt

cd src
python manage.py collectstatic --no-input
python manage.py migrate
