from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

from .models import Demand
from .serializers import DemandSerializer, DemandCreateSerializer, DemandUpdateSerializer


class DemandViewSet(viewsets.ModelViewSet):
    serializer_class = DemandSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        
        if user.role in ['DIRECTORY', 'SEDUC']:
            return Demand.objects.all().select_related('category', 'school', 'created_by')
        
        return Demand.objects.filter(school=user.school).select_related('category', 'school', 'created_by')

    def get_serializer_class(self):
        if self.action == 'create':
            return DemandCreateSerializer
        if self.action in ['update', 'partial_update']:
            return DemandUpdateSerializer
        return DemandSerializer

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=True, methods=['post'])
    def resolve(self, request, pk=None):
        demand = self.get_object()
        demand.status = 'COMPLETED'
        from django.utils import timezone
        demand.resolved_at = timezone.now()
        demand.save()
        return Response(DemandSerializer(demand).data)