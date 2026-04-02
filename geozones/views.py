from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Geozone, PointCheck
from .serializers import GeozoneSerializer, PointCheckSerializer
from .services import check_point_in_geozones


class GeozoneViewSet(viewsets.ModelViewSet):
    """
    1. Создать геозону: POST /api/geozones/
    2. Получить список: GET /api/geozones/
    """
    queryset = Geozone.objects.all()
    serializer_class = GeozoneSerializer

    @action(detail=False, methods=['post'], url_path='check-point')
    def check_point(self, request):
        """
        3. Проверить точку: POST /api/geozones/check-point/
        """
        # Валидация входных данных
        serializer = PointCheckSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        lat, lon = data['lat'], data['lon']

        # Логика PostGIS через сервис
        matched_zone = check_point_in_geozones(lat, lon)

        # Сохранение результата
        check_log = PointCheck.objects.create(
            device_id=data['device_id'],
            lat=lat,
            lon=lon,
            inside=bool(matched_zone),
            matched_geozone=matched_zone
        )

        return Response(PointCheckSerializer(check_log).data, status=status.HTTP_201_CREATED)


class PointCheckHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    4. Получить историю: GET /api/checks/
    Поддерживает фильтрацию по device_id и inside
    """
    queryset = PointCheck.objects.all()
    serializer_class = PointCheckSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['device_id', 'inside']