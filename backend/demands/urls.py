from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DemandViewSet, serve_attachment

router = DefaultRouter()
router.register('', DemandViewSet, basename='demand')

urlpatterns = [
    path('', include(router.urls)),
    path('attachments/<uuid:attachment_id>/', serve_attachment, name='serve-attachment'),
]