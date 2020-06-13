from django.db import models
from .host_virtuales import HostVirtual

class Aplicacion(models.Model):

    id = models.AutoField(primary_key=True, db_column='id')
    nombre = models.CharField(max_length=100, null=False, db_column='nombre')
    ruta_web = models.CharField(max_length=100, null=False, db_column='ruta_web')
    version = models.CharField(max_length=10, null=True, db_column='version')
    repositorio = models.CharField(max_length=255, null=True, db_column='repositorio')
    activo = models.BooleanField(default=True, db_column='activo')
    host_virtual = models.ForeignKey(HostVirtual, null=False, db_column='host_virtual_id', on_delete=models.CASCADE, related_name='aplicaciones')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:

        db_table = 'aplicaciones'