from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction

from categories.models import Category
from schools.models import School

User = get_user_model()

DEFAULT_ADMIN_EMAIL = "admin@escolavoz.com"
DEFAULT_ADMIN_PASSWORD = "admin123"
DEFAULT_ADMIN_USERNAME = "admin"

DEFAULT_USER_EMAIL = "user@escolavoz.com"
DEFAULT_USER_PASSWORD = "user123"
DEFAULT_USER_USERNAME = "user"

DEFAULT_CATEGORIES = [
    {"name": "Infraestrutura", "description": "Problemas de infraestrutura escolar"},
    {"name": "Merenda", "description": "Questões relacionadas à merenda escolar"},
    {"name": "Transporte", "description": "Demandas de transporte escolar"},
    {"name": "Material Didático", "description": "Solicitações de material didático"},
    {"name": "Recursos Humanos", "description": "Questões de pessoal e RH"},
    {"name": "TI", "description": "Demandas de tecnologia da informação"},
    {"name": "Segurança", "description": "Questões de segurança escolar"},
    {"name": "Outros", "description": "Demandas não categorizadas"},
]

DEFAULT_SCHOOLS = [
    {"name": "EMEF Prof. Antônio Carlos", "code": "ESC001", "city": "São Paulo"},
    {"name": "EMEF Maria Aparecida", "code": "ESC002", "city": "Campinas"},
    {"name": "EMEF José Bonifácio", "code": "ESC003", "city": "São Bernardo do Campo"},
    {"name": "EMEF Santos Dumont", "code": "ESC004", "city": "Guarulhos"},
    {"name": "EMEF Albert Einstein", "code": "ESC005", "city": "São Paulo"},
    {"name": "Diretoria de Ensino", "code": "DIRETORIA001", "city": "São Paulo"},
]


class Command(BaseCommand):
    help = "Cria dados padrão (usuários, categorias e escolas) caso não existam"

    @transaction.atomic
    def handle(self, *args, **options):
        created_users = []
        created_categories = []
        created_schools = []

        if not User.objects.filter(email=DEFAULT_ADMIN_EMAIL).exists():
            User.objects.create_superuser(
                email=DEFAULT_ADMIN_EMAIL,
                username=DEFAULT_ADMIN_USERNAME,
                password=DEFAULT_ADMIN_PASSWORD,
                first_name="Admin",
                last_name="Sistema",
            )
            created_users.append(f"admin ({DEFAULT_ADMIN_EMAIL})")

        if not User.objects.filter(email=DEFAULT_USER_EMAIL).exists():
            User.objects.create_user(
                email=DEFAULT_USER_EMAIL,
                username=DEFAULT_USER_USERNAME,
                password=DEFAULT_USER_PASSWORD,
                first_name="Usuário",
                last_name="Padrão",
            )
            created_users.append(f"user ({DEFAULT_USER_EMAIL})")

        for cat in DEFAULT_CATEGORIES:
            if not Category.objects.filter(name=cat["name"]).exists():
                Category.objects.create(**cat)
                created_categories.append(cat["name"])

        for school_data in DEFAULT_SCHOOLS:
            if not School.objects.filter(code=school_data["code"]).exists():
                School.objects.create(**school_data)
                created_schools.append(school_data["name"])

        admin_user = User.objects.filter(email=DEFAULT_ADMIN_EMAIL).first()
        if admin_user and admin_user.role != 'SEDUC':
            admin_user.role = 'SEDUC'
            admin_user.save(update_fields=['role'])
            self.stdout.write(self.style.SUCCESS(f"Admin atualizado para role SEDUC"))

        first_school = School.objects.filter(code__startswith='ESC').first()
        user_obj = User.objects.filter(email=DEFAULT_USER_EMAIL).first()
        if user_obj and first_school and user_obj.school_id != first_school.id:
            user_obj.school = first_school
            user_obj.save(update_fields=['school'])
            self.stdout.write(self.style.SUCCESS(f"User vinculado à escola {first_school.name}"))

        if created_users:
            self.stdout.write(self.style.SUCCESS(f"Usuários criados: {', '.join(created_users)}"))
        else:
            self.stdout.write(self.style.WARNING("Usuários padrão já existem"))

        if created_categories:
            self.stdout.write(self.style.SUCCESS(f"Categorias criadas: {', '.join(created_categories)}"))
        else:
            self.stdout.write(self.style.WARNING("Categorias padrão já existem"))

        if created_schools:
            self.stdout.write(self.style.SUCCESS(f"Escolas criadas: {', '.join(created_schools)}"))
        else:
            self.stdout.write(self.style.WARNING("Escolas padrão já existem"))
