from django.db import models
from .maquinas import Maquina

class UsuarioMaquina(models.Model):

    id = models.AutoField(primary_key=True, db_column='id')
    usuario = models.CharField(max_length=50, null=False, db_column='usuario')
    password = models.CharField(max_length=255, null=False, db_column='password')
    activo = models.BooleanField(null=False, default=True, db_column='activo')
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE, null=False)

    class Meta:

        db_table = 'usuario_maquinas'