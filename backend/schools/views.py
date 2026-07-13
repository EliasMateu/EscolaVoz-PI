from rest_framework import viewsets, permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS
from schools.repositories import SchoolRepository
from schools.serializers import SchoolSerializer


class ReadOnlyOrAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    permission_classes = [ReadOnlyOrAuthenticated]
    repository = SchoolRepository()

    def get_queryset(self):
        if self.request.method in SAFE_METHODS and not self.request.user.is_authenticated:
            return self.repository.get_all()

        user = self.request.user
        
        if user.role in ['DIRECTORY', 'SEDUC']:
            return self.repository.get_all()
        
        if user.school:
            return self.repository.get_by_id(str(user.school.id))
        
        return self.repository.get_all()

    def perform_create(self, serializer):
        if self.request.user.role not in ['SEDUC']:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied('Apenas SEDUC pode criar escolas')
        serializer.save()