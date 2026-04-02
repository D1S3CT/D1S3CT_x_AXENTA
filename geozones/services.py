from django.contrib.gis.geos import Point
from .models import Geozone


def check_point_in_geozones(lat: float, lon: float):
    """
    Выполняет поиск геозоны средствами PostGIS.
    Если геозон несколько, берем первую
    """
    point = Point(lon, lat, srid=4326)

    return Geozone.objects.filter(geometry__contains=point).first()