from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
import csv
from io import StringIO

from .models import School
from .serializers import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    @action(detail=False, methods=['post'])
    def verify_code(self, request):
        code = request.data.get('code')
        if not code:
            return Response({'error': 'Código é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            school = School.objects.get(code=code, is_active=True)
            return Response(SchoolSerializer(school).data)
        except School.DoesNotExist:
            return Response({'error': 'Código de escola inválido ou inativo.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'])
    def import_csv(self, request):
        if not request.user.is_staff:
            return Response({'error': 'Permissão negada.'}, status=status.HTTP_403_FORBIDDEN)
        
        csv_file = request.FILES.get('file')
        if not csv_file:
            return Response({'error': 'Arquivo CSV é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            decoded = csv_file.read().decode('utf-8')
            reader = csv.DictReader(StringIO(decoded))
            
            schools_created = 0
            schools_updated = 0
            
            for row in reader:
                code = row.get('code', '').strip()
                name = row.get('name', '').strip()
                
                if not code or not name:
                    continue
                
                school, created = School.objects.update_or_create(
                    code=code,
                    defaults={
                        'name': name,
                        'address': row.get('address', '').strip(),
                        'city': row.get('city', '').strip(),
                        'director_email': row.get('director_email', '').strip(),
                    }
                )
                
                if created:
                    schools_created += 1
                else:
                    schools_updated += 1
            
            return Response({
                'message': f'Importação concluída: {schools_created} criadas, {schools_updated} atualizadas.'
            })
        except Exception as e:
            return Response({'error': f'Erro ao processar arquivo: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)