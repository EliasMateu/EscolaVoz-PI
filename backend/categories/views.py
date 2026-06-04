from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from categories.repositories import CategoryRepository
from categories.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    repository = CategoryRepository()

    def get_queryset(self):
        user = self.request.user
        
        if user.role in ['DIRECTORY', 'SEDUC']:
            return self.repository.get_all()
        
        return self.repository.get_active()
    
    def create(self, request, *args, **kwargs):
        if not request.user.role in ['SEDUC']:
            return Response(
                {'error': 'Apenas SEDUC pode criar categorias'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = self.repository.create(serializer.validated_data)
        return Response(CategorySerializer(category).data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        if not request.user.role in ['SEDUC']:
            return Response(
                {'error': 'Apenas SEDUC pode editar categorias'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.pop('partial', False))
        serializer.is_valid(raise_exception=True)
        category = self.repository.update(instance, serializer.validated_data)
        return Response(CategorySerializer(category).data)
    
    def destroy(self, request, *args, **kwargs):
        if not request.user.role in ['SEDUC']:
            return Response(
                {'error': 'Apenas SEDUC pode excluir categorias'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        return super().destroy(request, *args, **kwargs)