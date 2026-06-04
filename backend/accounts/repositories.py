from typing import Optional
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()


class UserRepository:
    
    def get_by_email(self, email: str) -> Optional[User]:
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
    
    def get_by_id(self, user_id: str) -> Optional[User]:
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
    
    def get_by_cpf(self, cpf: str) -> Optional[User]:
        try:
            return User.objects.get(cpf=cpf)
        except User.DoesNotExist:
            return None
    
    def create_user(self, email: str, cpf: str, first_name: str, 
                    last_name: str, password: str, school_code: str = None) -> User:
        from schools.models import School
        
        school = None
        if school_code:
            school = School.objects.filter(code=school_code).first()
        
        user = User(
            email=email,
            cpf=cpf,
            first_name=first_name,
            last_name=last_name,
            school=school,
            role=school.code if school and school.code.startswith('DIRETORIA') else 'EMPLOYEE' if school else 'EMPLOYEE'
        )
        
        if school_code and not school:
            from schools.models import School
            from django.contrib.auth.models import Group
            
            school = School.objects.filter(code__startswith='ESC').first()
            if school:
                user.school = school
                
                try:
                    director_group = Group.objects.get(name='Diretor')
                    user.groups.add(director_group)
                    user.role = 'PRINCIPAL'
                except Group.DoesNotExist:
                    pass
        
        user.set_password(password)
        
        try:
            user.save()
        except IntegrityError:
            raise ValidationException("CPF ou email já cadastrado")
        
        return user