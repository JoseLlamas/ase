
from django.db import models

class Maquina(models.Model):

    TIPO_CHOICES = (
        ('C', 'Cliente'),
        ('S', 'Servidor')
    )

    id = models.AutoField(db_column='id', primary_key=True)
    sistema_operativo = models.CharField(db_column='sistema_operativo', max_length=100, null=False)
    nombre = models.CharField(db_column='nombre', max_length=30, null=False)
    activo = models.BooleanField(default=True, db_column='activo')
    tipo = models.CharField(choices=TIPO_CHOICES, null=False, max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:

        db_table = 'maquinas'
        