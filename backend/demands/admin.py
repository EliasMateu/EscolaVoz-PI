from django.contrib import admin
from .models import Demand


@admin.register(Demand)
class DemandAdmin(admin.ModelAdmin):
    list_display = ['title', 'school', 'category', 'status', 'priority', 'created_by', 'created_at']
    list_filter = ['status', 'priority', 'category', 'school']
    search_fields = ['title', 'description']
    ordering = ['-created_at']