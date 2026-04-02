from django.contrib.gis.geos import Polygon, Point
from django.test import TestCase
from rest_framework.test import APIClient
from geozones.models import Geozone

class GeozoneAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Создаю тестовый квадрат 10x10 градусов
        self.zone = Geozone.objects.create(
            name="Test Zone",
            geometry=Polygon(((0, 0), (0, 10), (10, 10), (10, 0), (0, 0)))
        )

    def test_check_point_inside(self):
        """Проверка точки внутри зоны"""
        response = self.client.post('/api/geozones/check-point/', {
            "device_id": "test-device",
            "lat": 5,
            "lon": 5
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data['inside'])
        self.assertEqual(response.data['matched_geozone']['name'], "Test Zone")

    def test_check_point_outside(self):
        """Проверка точки снаружи зоны"""
        response = self.client.post('/api/geozones/check-point/', {
            "device_id": "test-device",
            "lat": 15,
            "lon": 15
        })
        self.assertEqual(response.status_code, 201)
        self.assertFalse(response.data['inside'])
        self.assertIsNone(response.data['matched_geozone'])