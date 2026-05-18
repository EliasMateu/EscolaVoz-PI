from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'cpf', 'first_name', 'last_name', 'role', 'school', 'is_active']
    list_filter = ['role', 'is_active', 'school']
    search_fields = ['email', 'cpf', 'first_name', 'last_name']
    ordering = ['-date_joined']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {'fields': ('cpf', 'role', 'school')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações Adicionais', {'fields': ('cpf', 'role', 'school')}),
    )