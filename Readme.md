# Geo-fencing API Service

Сервис для создания геозон (полигонов) и проверки вхождения точек в эти зоны.

## Как запустить
1. Соберите проект: `docker-compose up --build -d`
2. Примените миграции: `docker-compose exec app python manage.py migrate`
3. Запустите тесты: `docker-compose exec app python manage.py test`

## Архитектурные особенности
- **PostGIS**: Геометрические вычисления проводятся на стороне БД.
- **Service Layer**: Бизнес-логика изолирована от контроллеров (views).
- **DRF**: Использованы ViewSets для лаконичного описания API.
- **Linter**: Код проверен с помощью Ruff и Black.