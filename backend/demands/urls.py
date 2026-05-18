from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DemandViewSet

router = DefaultRouter()
router.register('', DemandViewSet, basename='demand')

urlpatterns = [
    path('', include(router.urls)),
]