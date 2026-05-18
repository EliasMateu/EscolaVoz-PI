from typing import Optional
from django.db.models import QuerySet
from demands.models import Demand, DemandAttachment


class DemandRepository:
    
    def get_all(self) -> QuerySet:
        return Demand.objects.all()
    
    def get_by_id(self, demand_id: str) -> Optional[Demand]:
        try:
            return Demand.objects.select_related(
                'category', 'school', 'created_by'
            ).get(id=demand_id)
        except Demand.DoesNotExist:
            return None
    
    def get_by_school(self, school_id: str) -> QuerySet:
        return Demand.objects.filter(school=school_id).select_related(
            'category', 'school', 'created_by'
        )
    
    def create(self, **kwargs) -> Demand:
        return Demand.objects.create(**kwargs)
    
    def update(self, demand: Demand, **kwargs) -> Demand:
        for key, value in kwargs.items():
            if value is not None:
                setattr(demand, key, value)
        demand.save()
        return demand
    
    def delete(self, demand: Demand) -> bool:
        demand.delete()
        return True
    
    def create_attachment(self, demand: Demand, file_data: str, file_name: str, 
                          content_type: str, file_size: int) -> DemandAttachment:
        return DemandAttachment.objects.create(
            demand=demand,
            file_data=file_data,
            file_name=file_name,
            content_type=content_type,
            file_size=file_size
        )