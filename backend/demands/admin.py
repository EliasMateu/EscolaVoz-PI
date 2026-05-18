from django.contrib import admin
from .models import Demand, DemandAttachment


@admin.register(Demand)
class DemandAdmin(admin.ModelAdmin):
    list_display = ['title', 'school', 'category', 'status', 'priority', 'created_by', 'created_at']
    list_filter = ['status', 'priority', 'category', 'school']
    search_fields = ['title', 'description']
    ordering = ['-created_at']


@admin.register(DemandAttachment)
class DemandAttachmentAdmin(admin.ModelAdmin):
    list_display = ['file_name', 'demand', 'content_type', 'file_size', 'created_at']
    list_filter = ['content_type', 'created_at']
    search_fields = ['file_name', 'demand__title']
    ordering = ['-created_at']