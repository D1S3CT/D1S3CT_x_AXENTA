from django.urls import path, include
from rest_framework.routers import DefaultRouter
from geozones.views import GeozoneViewSet, PointCheckHistoryViewSet

router = DefaultRouter()
router.register(r'geozones', GeozoneViewSet, basename='geozone')
router.register(r'checks', PointCheckHistoryViewSet, basename='check')

urlpatterns = [
    path('api/', include(router.urls)),
]