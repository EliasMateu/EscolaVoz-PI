from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    school_name = serializers.CharField(source='school.name', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'cpf', 'first_name', 'last_name', 'role', 'school', 'school_name', 'is_active', 'date_joined']
        read_only_fields = ['id', 'date_joined']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True)
    school_code = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['email', 'cpf', 'first_name', 'last_name', 'password', 'password_confirm', 'school_code']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({'password': 'As senhas não coincidem.'})
        
        if attrs.get('cpf'):
            if User.objects.filter(cpf=attrs['cpf']).exists():
                raise serializers.ValidationError({'cpf': 'Este CPF já está em uso.'})
        
        if attrs.get('email') and User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email': 'Este email já está em uso.'})

        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm', None)
        school_code = validated_data.pop('school_code', None)
        
        user = User.objects.create_user(
            username=validated_data.get('email') or validated_data.get('cpf'),
            **validated_data
        )
        
        if school_code:
            from schools.models import School
            try:
                school = School.objects.get(code=school_code)
                user.school = school
                user.save()
            except School.DoesNotExist:
                pass
        
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, validators=[validate_password])

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Senha atual incorreta.')
        return value