from rest_framework import serializers
from .models import School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'code', 'address', 'city', 'director_email', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class SchoolCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=20)

    def validate_code(self, value):
        if not School.objects.filter(code=value, is_active=True).exists():
            raise serializers.ValidationError('Código de escola inválido ou inativo.')
        return value