from django.db import models
from .maquinas import Maquina

class Servidor(models.Model):

    id = models.AutoField(primary_key=True, db_column='id')
    modo = models.CharField(max_length=100, db_column='modo', null=True)
    nombre = models.CharField(max_length=100, db_column='nombre', null=False)
    version = models.CharField(max_length=10, db_column='version', null=False)
    root_path = models.CharField(max_length=255, db_column='root', null=True)
    puerto_admin = models.IntegerField(db_column='puerto_admin', null=True)
    usuario_admin = models.CharField(db_column='usuario_admin', null=True, max_length=50)
    password_admin = models.CharField(db_column='password_admin', null=True, max_length=255)
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE, null=False, db_column='maquina_id', related_name='servidores')
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    objects = models.Manager()

    class Meta:

        db_table = 'servidores'
