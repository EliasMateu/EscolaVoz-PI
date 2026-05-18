from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Count, Sum
from demands.models import Demand
from schools.models import School
from categories.models import Category


class DashboardStatsView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        
        if user.role in ['DIRECTORY', 'SEDUC']:
            demands = Demand.objects.all()
        else:
            demands = Demand.objects.filter(school=user.school)
        
        total = demands.count()
        pending = demands.filter(status='PENDING').count()
        in_progress = demands.filter(status='IN_PROGRESS').count()
        completed = demands.filter(status='COMPLETED').count()
        rejected = demands.filter(status='REJECTED').count()
        
        return Response({
            'total': total,
            'pending': pending,
            'in_progress': in_progress,
            'completed': completed,
            'rejected': rejected
        })


class DashboardByCategoryView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        
        if user.role in ['DIRECTORY', 'SEDUC']:
            demands = Demand.objects.all()
        else:
            demands = Demand.objects.filter(school=user.school)
        
        data = demands.values('category__name').annotate(count=Count('id'))
        
        return Response({item['category__name'] or 'Sem categoria': item['count'] for item in data})


class DashboardBySchoolView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        
        if user.role in ['DIRECTORY', 'SEDUC']:
            demands = Demand.objects.all()
        else:
            return Response({'error': 'Acesso restrito'}, status=403)
        
        data = demands.values('school__name').annotate(count=Count('id'))
        
        return Response({item['school__name']: item['count'] for item in data})


class DashboardExportView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        
        if user.role not in ['DIRECTORY', 'SEDUC']:
            return Response({'error': 'Acesso restrito'}, status=403)
        
        demands = Demand.objects.all().select_related('category', 'school', 'created_by')
        
        import csv
        import io
        from django.http import HttpResponse
        
        output = io.StringIO()
        writer = csv.writer(output)
        
        writer.writerow(['ID', 'Título', 'Categoria', 'Escola', 'Status', 'Prioridade', 'Criado por', 'Data Criação'])
        
        for d in demands:
            writer.writerow([
                str(d.id),
                d.title,
                d.category.name if d.category else '',
                d.school.name if d.school else '',
                d.status,
                d.priority,
                d.created_by.get_full_name() if d.created_by else '',
                d.created_at.strftime('%Y-%m-%d %H:%M')
            ])
        
        return Response({'csv': output.getvalue()})