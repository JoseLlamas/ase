
from django.db import models

class Maquina(models.Model):

    TIPO_CHOISES = (
        ('C', 'Cliente'),
        ('S', 'Servidor')
    )

    id = models.AutoField(db_column='id', primary_key=True)
    sistema_operativo = models.CharField(db_column='sistema_operativo', max_length=100, null=False)
    nombre = models.CharField(db_column='nombre', max_length=30, null=False)
    activo = models.BooleanField(default=True, db_column='activo', null=False)
    tipo = models.CharField(choices=TIPO_CHOISES, null=False, max_length=1)

    class Meta:

        db_table = 'maquinas'
        