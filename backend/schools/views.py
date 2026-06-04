from rest_framework import viewsets, permissions
from schools.repositories import SchoolRepository
from schools.serializers import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    permission_classes = [permissions.IsAuthenticated]
    repository = SchoolRepository()

    def get_queryset(self):
        user = self.request.user
        
        if user.role in ['DIRECTORY', 'SEDUC']:
            return self.repository.get_all()
        
        if user.school:
            return self.repository.get_by_id(str(user.school.id))
        
        return self.repository.get_all()

    def create(self, request, *args, **kwargs):
        if not request.user.role in ['SEDUC']:
            from rest_framework.response import Response
            from rest_framework import status
            return Response(
                {'error': 'Apenas SEDUC pode criar escolas'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        school = self.repository.create(serializer.validated_data)
        return Response(SchoolSerializer(school).data, status=status.HTTP_201_CREATED)