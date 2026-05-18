from rest_framework import serializers
from .models import Demand
from categories.serializers import CategorySerializer
from schools.serializers import SchoolSerializer


class DemandSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    school_name = serializers.CharField(source='school.name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)

    class Meta:
        model = Demand
        fields = [
            'id', 'title', 'description', 'category', 'category_name',
            'school', 'school_name', 'created_by', 'created_by_name',
            'status', 'priority', 'created_at', 'updated_at', 'resolved_at'
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at', 'resolved_at']


class DemandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = ['title', 'description', 'category', 'priority']

    def create(self, validated_data):
        validated_data['school'] = self.context['request'].user.school
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)


class DemandUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = ['title', 'description', 'category', 'status', 'priority']