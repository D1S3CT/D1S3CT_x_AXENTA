from rest_framework import serializers
from django.contrib.gis.geos import GEOSGeometry
from .models import Geozone, PointCheck

class GeozoneShortSerializer(serializers.ModelSerializer):
    """Для вложенного ответа в результатах проверки"""
    class Meta:
        model = Geozone
        fields = ['id', 'name']

class GeozoneSerializer(serializers.ModelSerializer):
    """Для полноценной работы с геозонами"""
    class Meta:
        model = Geozone
        fields = ['id', 'name', 'geometry']

class PointCheckSerializer(serializers.ModelSerializer):
    # Использую сокращенный сериализатор для красивого ответа по ТЗ
    matched_geozone = GeozoneShortSerializer(read_only=True)

    class Meta:
        model = PointCheck
        fields = ['id', 'device_id', 'lat', 'lon', 'inside', 'matched_geozone', 'created_at']
        # Поля, которые клиент не должен присылать сам
        read_only_fields = ['inside', 'matched_geozone', 'created_at']