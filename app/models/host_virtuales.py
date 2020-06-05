from django.db import models
from .servidores import Servidor

class HostVirtual(models.Model):

    id = models.AutoField(primary_key=True, db_column='id')
    nombre = models.CharField(max_length=100, db_column='nombre', null='False', default='0.0.0.0')
    puerto = models.IntegerField(null=False, db_column='puerto', default=80)
    default = models.BooleanField(db_column='default', default=False)
    activo = models.BooleanField(db_column="activo", default=True)
    servidor = models.ForeignKey(Servidor, null=False, on_delete=models.CASCADE, db_column='servidor_id', related_name='host_virtuales')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:

        db_table = 'host_virtuales'