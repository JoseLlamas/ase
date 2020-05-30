from django.db import models
from .maquinas import Maquina

class Ip(models.Model):

    id = models.AutoField(primary_key=True, db_column='id')
    ip = models.CharField(max_length=15, null=False, db_column='ip')
    interfaz = models.CharField(max_length=10, null=True, db_column='interfaz')
    mac = models.CharField(max_length=100, null=False, db_column='mac_address')
    activo = models.BooleanField(default=True, db_column="activo")
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE, null=False, related_name='ips', db_column='maquina_id')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:

        db_table = 'ips'
        