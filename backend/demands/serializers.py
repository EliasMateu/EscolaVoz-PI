from rest_framework import serializers
from .models import Demand
from categories.serializers import CategorySerializer
from schools.serializers import SchoolSerializer
from schools.models import School


class DemandSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    school_name = serializers.CharField(source='school.name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Demand
        fields = [
            'id', 'title', 'description', 'category', 'category_name',
            'school', 'school_name', 'created_by', 'created_by_name',
            'status', 'priority', 'image', 'image_url',
            'created_at', 'updated_at', 'resolved_at'
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at', 'resolved_at', 'image_url']

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class DemandCreateSerializer(serializers.ModelSerializer):
    school = serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Demand
        fields = ['title', 'description', 'category', 'priority', 'image', 'school']

    def validate_priority(self, value):
        user = self.context['request'].user
        if user.role not in ['DIRECTORY', 'SEDUC']:
            return 'MEDIUM'
        return value


class DemandUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = ['title', 'description', 'category', 'status', 'priority', 'image']
        extra_kwargs = {
            'image': {'required': False},
        }

    def validate_image(self, value):
        return value

    def update(self, instance, validated_data):
        image = validated_data.get('image')
        
        if image == '' or image is None:
            if instance.image:
                instance.image.delete(save=False)
                instance.image = None
        
        return super().update(instance, validated_data)