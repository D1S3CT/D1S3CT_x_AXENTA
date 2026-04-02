#!/bin/bash

# Ожидание доступности базы данных
echo "Waiting for postgres..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

# Применение миграций
echo "Applying migrations..."
python manage.py migrate

# Запуск сервера
echo "Starting server..."
python manage.py runserver 0.0.0.0:8000