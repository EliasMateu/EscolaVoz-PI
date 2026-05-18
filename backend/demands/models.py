import uuid
from django.db import models
from django.conf import settings


class DemandStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pendente'
    IN_PROGRESS = 'IN_PROGRESS', 'Em Andamento'
    COMPLETED = 'COMPLETED', 'Concluído'
    REJECTED = 'REJECTED', 'Rejeitado'


class DemandPriority(models.TextChoices):
    LOW = 'LOW', 'Baixa'
    MEDIUM = 'MEDIUM', 'Média'
    HIGH = 'HIGH', 'Alta'
    URGENT = 'URGENT', 'Urgente'


class Demand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, verbose_name='Título')
    description = models.TextField(blank=True, verbose_name='Descrição')
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.PROTECT,
        related_name='demands',
        verbose_name='Categoria'
    )
    school = models.ForeignKey(
        'schools.School',
        on_delete=models.CASCADE,
        related_name='demands',
        verbose_name='Escola'
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_demands',
        verbose_name='Criado por'
    )
    status = models.CharField(
        max_length=20,
        choices=DemandStatus.choices,
        default=DemandStatus.PENDING,
        verbose_name='Status'
    )
    priority = models.CharField(
        max_length=20,
        choices=DemandPriority.choices,
        default=DemandPriority.MEDIUM,
        verbose_name='Prioridade'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True, verbose_name='Resolvido em')

    class Meta:
        verbose_name = 'Demanda'
        verbose_name_plural = 'Demandas'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} - {self.school.name}'