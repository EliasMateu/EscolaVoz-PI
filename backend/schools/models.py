import uuid
from django.db import models


class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name='Nome da Escola')
    code = models.CharField(max_length=20, unique=True, verbose_name='Código')
    address = models.CharField(max_length=500, blank=True, verbose_name='Endereço')
    city = models.CharField(max_length=100, blank=True, verbose_name='Cidade')
    director_email = models.EmailField(blank=True, verbose_name='Email do Diretor')
    is_active = models.BooleanField(default=True, verbose_name='Ativa')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Escola'
        verbose_name_plural = 'Escolas'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.code})'