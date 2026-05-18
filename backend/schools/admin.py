from django.contrib import admin
from .models import School


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'city', 'director_email', 'is_active']
    list_filter = ['is_active', 'city']
    search_fields = ['name', 'code', 'city']
    ordering = ['name']