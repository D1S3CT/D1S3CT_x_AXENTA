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

## Примеры запросов (API Examples)

Для тестирования через терминал (Git Bash / Terminal) используйте следующие команды:

### 1. Создание геозоны
```bash
curl -X POST http://localhost:8000/api/geozones/ \
-H "Content-Type: application/json" \
-d '{"name": "Test Warehouse", "geometry": "POLYGON ((50.10 53.20, 50.20 53.20, 50.20 53.30, 50.10 53.30, 50.10 53.20))"}'
```

### 2. Проверка точки (Внутри зоны)
```bash
curl -X POST http://localhost:8000/api/geozones/check-point/ \
-H "Content-Type: application/json" \
-d '{"device_id": "truck-001", "lat": 53.25, "lon": 50.15}'
```

### 3. Проверка точки (Снаружи зоны)
```bash
curl -X POST http://localhost:8000/api/geozones/check-point/ \
-H "Content-Type: application/json" \
-d '{"device_id": "truck-001", "lat": 54.0, "lon": 51.0}'
```

### 4. Получение истории проверок
```bash
curl -X GET "http://localhost:8000/api/checks/?device_id=truck-001"
```
