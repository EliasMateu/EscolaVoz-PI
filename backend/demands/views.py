from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.http import HttpResponse

from .models import Demand, DemandAttachment
from .serializers import DemandSerializer, DemandCreateSerializer, DemandUpdateSerializer
from .services import DemandService
from .exceptions import (
    DemandNotFoundException,
    DemandPermissionException,
    DemandValidationException
)


class DemandViewSet(viewsets.ModelViewSet):
    
    serializer_class = DemandSerializer
    permission_classes = [permissions.IsAuthenticated]
    service = DemandService()
    
    def get_queryset(self):
        return self.service.get_demands_for_user(self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return DemandCreateSerializer
        if self.action in ['update', 'partial_update']:
            return DemandUpdateSerializer
        return DemandSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            demand = self.service.create_demand(serializer.validated_data, request.user)
            return Response(DemandSerializer(demand).data, status=status.HTTP_201_CREATED)
        except DemandValidationException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=kwargs.pop('partial', False))
            serializer.is_valid(raise_exception=True)
            demand = self.service.update_demand(str(instance.id), serializer.validated_data, request.user)
            return Response(DemandSerializer(demand).data)
        except (DemandPermissionException, DemandValidationException) as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.service.delete_demand(str(instance.id), request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except DemandPermissionException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'])
    def resolve(self, request, pk=None):
        try:
            demand = self.service.resolve_demand(pk, request.user)
            return Response(DemandSerializer(demand).data)
        except DemandPermissionException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DemandStatisticsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    service = DemandService()
    
    def get(self, request):
        return Response(self.service.get_statistics(request.user))


@api_view(['GET'])
@permission_classes([AllowAny])
def serve_attachment(request, attachment_id):
    try:
        attachment = DemandAttachment.objects.get(id=attachment_id)
        return HttpResponse(attachment.file_data, content_type=attachment.content_type)
    except DemandAttachment.DoesNotExist:
        return HttpResponse(status=404)