from django.db.models import QuerySet
from demands.models import Demand


class DashboardRepository:
    
    def get_all_demands(self) -> QuerySet:
        return Demand.objects.all()
    
    def get_by_school(self, school_id: str) -> QuerySet:
        return Demand.objects.filter(school_id=school_id)