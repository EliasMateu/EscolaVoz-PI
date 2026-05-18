from django.db.models import QuerySet
from schools.models import School


class SchoolRepository:
    
    def get_all(self) -> QuerySet:
        return School.objects.all()
    
    def get_by_id(self, school_id: str) -> QuerySet:
        return School.objects.filter(id=school_id)
    
    def get_by_code(self, code: str) -> School:
        try:
            return School.objects.get(code=code)
        except School.DoesNotExist:
            return None
    
    def create(self, data: dict) -> School:
        return School.objects.create(**data)
    
    def update(self, school: School, data: dict) -> School:
        for key, value in data.items():
            setattr(school, key, value)
        school.save()
        return school