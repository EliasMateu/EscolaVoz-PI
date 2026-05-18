from django.db.models import QuerySet
from categories.models import Category


class CategoryRepository:
    
    def get_all(self) -> QuerySet:
        return Category.objects.all()
    
    def get_active(self) -> QuerySet:
        return Category.objects.filter(is_active=True)
    
    def get_by_id(self, category_id: str) -> Category:
        return Category.objects.get(id=category_id)
    
    def create(self, data: dict) -> Category:
        return Category.objects.create(**data)
    
    def update(self, category: Category, data: dict) -> Category:
        for key, value in data.items():
            setattr(category, key, value)
        category.save()
        return category
    
    def delete(self, category: Category) -> bool:
        category.delete()
        return True