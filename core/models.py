from django.db import models
from django.contrib.auth.models import User

# Indicadores individuales
class Indicator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='Hectáreas en Restauración')
    value = models.FloatField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}: {self.value} ({self.user.username})"

# Propuestas de proyecto
class ProjectProposal(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    proposer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} — {self.proposer.username}"

# Perfil extendido del usuario
class Profile(models.Model):
    ROLE_CHOICES = [
        ('admin_territorial', 'Administrador Territorial'),
        ('company_small', 'Empresa Pequeña'),
        ('company_large', 'Empresa Grande'),
        ('environmental_intermediary', 'Intermediario Ambiental'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='admin_territorial')

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"

# riesgos
class Risk(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Usuario que reporta este riesgo"
    )
    is_territory = models.BooleanField(
        default=False,
        help_text="¿Es un riesgo general del territorio?"
    )
    name = models.CharField(
        max_length=200,
        help_text="Nombre o título del riesgo"
    )
    residual = models.TextField(
        help_text="Elemento residual del riesgo que no se puede mitigar"
    )
    financial_impact = models.DecimalField(
        "Impacto financiero",
        max_digits=12,
        decimal_places=2,
        help_text="Impacto en las cuentas financieras"
    )
    csv_file = models.FileField(
        upload_to='risks_csv/',
        blank=True,
        help_text="Carga un CSV con detalles adicionales"
    )
    gpt_link = models.URLField(
        blank=True,
        help_text="Enlace a tu modelo GPT personalizado para análisis ágil"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.owner.username})"

#indicadores de resiliencia
class ResilienceIndicator(models.Model):
    name = models.CharField(max_length=200, help_text="Nombre del indicador")
    description = models.TextField(blank=True, help_text="Descripción opcional")
    unit = models.CharField(max_length=50, help_text="Unidad de medida (ej: hectáreas, %)")
    baseline = models.FloatField(help_text="Línea base del indicador")
    target = models.FloatField(help_text="Meta esperada")
    year_target = models.PositiveIntegerField(help_text="Año meta")
    risk_focus = models.CharField(max_length=200, help_text="Riesgo principal al que responde")
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.unit})"

#proyectos

class Project(models.Model):
    STATUS_CHOICES = [
        ('formulation', 'En Formulación'),
        ('active', 'Activo'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    indicator = models.CharField(max_length=100, help_text="Indicador objetivo")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='formulation')
    proposer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"


# Perfil extendido del usuario
class Profile(models.Model):
    ROLE_CHOICES = [
        ('platform_admin',         'Administrador de Plataforma'),
        ('admin_territorial',      'Administrador Territorial'),
        ('company_small',          'Empresa Pequeña'),
        ('company_large',          'Empresa Grande'),
        ('environmental_intermediary', 'Intermediario Ambiental'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='admin_territorial')

    # Nuevos campos
    description = models.TextField(blank=True, help_text="Descripción del intermediario")
    rating = models.FloatField(default=0, help_text="Puntuación promedio")
    projects_done = models.PositiveIntegerField(default=0, help_text="Número de proyectos realizados")

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"

