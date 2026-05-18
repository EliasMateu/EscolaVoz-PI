from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.db.models import Count
from django.http import HttpResponse
import csv
from io import StringIO

from demands.models import Demand
from schools.models import School
from categories.models import Category


class IsAdminOrDirectory(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['DIRECTORY', 'SEDUC']


class DashboardStatsView(APIView):
    permission_classes = [IsAdminOrDirectory]

    def get(self, request):
        demands = Demand.objects.all()
        
        total = demands.count()
        pending = demands.filter(status='PENDING').count()
        in_progress = demands.filter(status='IN_PROGRESS').count()
        completed = demands.filter(status='COMPLETED').count()
        rejected = demands.filter(status='REJECTED').count()

        by_priority = demands.values('priority').annotate(count=Count('id'))
        
        return Response({
            'total': total,
            'by_status': {
                'pending': pending,
                'in_progress': in_progress,
                'completed': completed,
                'rejected': rejected,
            },
            'by_priority': {item['priority']: item['count'] for item in by_priority},
        })


class DashboardByCategoryView(APIView):
    permission_classes = [IsAdminOrDirectory]

    def get(self, request):
        by_category = Demand.objects.values('category__name').annotate(count=Count('id'))
        
        return Response({
            'by_category': [{'category': item['category__name'], 'count': item['count']} for item in by_category]
        })


class DashboardBySchoolView(APIView):
    permission_classes = [IsAdminOrDirectory]

    def get(self, request):
        by_school = Demand.objects.values('school__name').annotate(count=Count('id'))
        
        return Response({
            'by_school': [{'school': item['school__name'], 'count': item['count']} for item in by_school]
        })


class DashboardExportView(APIView):
    permission_classes = [IsAdminOrDirectory]

    def get(self, request):
        demands = Demand.objects.all().select_related('category', 'school', 'created_by')
        
        output = StringIO()
        writer = csv.writer(output)
        
        writer.writerow([
            'ID', 'Título', 'Descrição', 'Categoria', 'Escola',
            'Criado por', 'Status', 'Prioridade', 'Data criação', 'Data resolução'
        ])
        
        for d in demands:
            writer.writerow([
                str(d.id),
                d.title,
                d.description or '',
                d.category.name,
                d.school.name,
                d.created_by.get_full_name() or d.created_by.email,
                d.status,
                d.priority,
                d.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                d.resolved_at.strftime('%Y-%m-%d %H:%M:%S') if d.resolved_at else '',
            ])
        
        output.seek(0)
        
        response = HttpResponse(output.getvalue(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="demandas.csv"'
        
        return response