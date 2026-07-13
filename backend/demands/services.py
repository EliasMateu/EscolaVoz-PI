from typing import Optional, List, Dict, Any
from django.utils import timezone
from demands.models import Demand
from demands.repositories import DemandRepository
from demands.exceptions import (
    DemandNotFoundException,
    DemandPermissionException,
    DemandValidationException
)


class DemandService:
    
    def __init__(self):
        self.repository = DemandRepository()
    
    def get_demands_for_user(self, user) -> List[Demand]:
        if user.role in ['DIRECTORY', 'SEDUC']:
            return list(self.repository.get_all())
        return list(self.repository.get_by_school(user.school))
    
    def get_demand_by_id(self, demand_id: str, user) -> Demand:
        demand = self.repository.get_by_id(demand_id)
        
        if not demand:
            raise DemandNotFoundException("Demanda não encontrada")
        
        if user.role not in ['DIRECTORY', 'SEDUC']:
            if demand.school_id != user.school_id:
                raise DemandPermissionException("Sem permissão para ver esta demanda")
        
        return demand
    
    def create_demand(self, data: Dict[str, Any], user) -> Demand:
        if not data.get('title'):
            raise DemandValidationException("Título é obrigatório")
        
        if not data.get('category'):
            raise DemandValidationException("Categoria é obrigatória")
        
        priority = data.get('priority', 'MEDIUM')
        if user.role not in ['DIRECTORY', 'SEDUC']:
            priority = 'MEDIUM'
        
        if user.role in ['DIRECTORY', 'SEDUC']:
            school = data.get('school')
            if not school:
                raise DemandValidationException("Escola é obrigatória")
        else:
            school = user.school
            if not school:
                raise DemandValidationException("Usuário não vinculado a nenhuma escola")
        
        return self.repository.create(
            title=data['title'],
            description=data.get('description', ''),
            category_id=data['category'].id if hasattr(data['category'], 'id') else data['category'],
            priority=priority,
            image=data.get('image'),
            school=school,
            created_by=user
        )
    
    def update_demand(self, demand_id: str, data: Dict[str, Any], user) -> Demand:
        demand = self.get_demand_by_id(demand_id, user)
        
        if user.role not in ['DIRECTORY', 'SEDUC']:
            if data.get('status') or data.get('priority'):
                raise DemandPermissionException("Apenas admin pode alterar status e prioridade")
        
        if data.get('title') is not None:
            demand.title = data['title']
        
        if data.get('description') is not None:
            demand.description = data['description']
        
        if data.get('category') is not None:
            demand.category_id = data['category'].id if hasattr(data['category'], 'id') else data['category']
        
        if 'image' in data:
            if data.get('removeImage'):
                if demand.image:
                    demand.image.delete(save=False)
                    demand.image = None
            elif data['image']:
                demand.image = data['image']
        
        if user.role in ['DIRECTORY', 'SEDUC']:
            if data.get('status') is not None:
                demand.status = data['status']
                if data['status'] == 'COMPLETED':
                    demand.resolved_at = timezone.now()
            
            if data.get('priority') is not None:
                demand.priority = data['priority']
        
        demand.save()
        return demand
    
    def delete_demand(self, demand_id: str, user) -> bool:
        demand = self.get_demand_by_id(demand_id, user)
        
        if user.role not in ['DIRECTORY', 'SEDUC']:
            raise DemandPermissionException("Apenas admin pode excluir demandas")
        
        return self.repository.delete(demand)
    
    def resolve_demand(self, demand_id: str, user) -> Demand:
        demand = self.get_demand_by_id(demand_id, user)
        
        if user.role not in ['DIRECTORY', 'SEDUC']:
            raise DemandPermissionException("Apenas admin pode resolver demandas")
        
        demand.status = 'COMPLETED'
        demand.resolved_at = timezone.now()
        demand.save()
        
        return demand
    
    def get_statistics(self, user) -> Dict[str, Any]:
        demands = self.get_demands_for_user(user)
        
        return {
            'total': len(demands),
            'pending': sum(1 for d in demands if d.status == 'PENDING'),
            'in_progress': sum(1 for d in demands if d.status == 'IN_PROGRESS'),
            'completed': sum(1 for d in demands if d.status == 'COMPLETED'),
            'rejected': sum(1 for d in demands if d.status == 'REJECTED')
        }