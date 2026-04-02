from django.contrib.gis.db import models


class Geozone(models.Model):
    """Сущность геозоны"""
    name = models.CharField(max_length=255)
    geometry = models.PolygonField(srid=4326)

    def __str__(self):
        return self.name


class PointCheck(models.Model):
    """Сущность проверки точки"""
    device_id = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()

    matched_geozone = models.ForeignKey(
        Geozone,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    inside = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)