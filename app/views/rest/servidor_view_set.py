from rest_framework import serializers, viewsets
from app.models import Servidor

class ServidorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Servidor
        fields = [
            'id',
            'modo',
            'nombre',
            'maquina_id',
            'version',
            'root_path',
            'puerto_admin',
            'usuario_admin',
            'password_admin'
        ]

class ServidorViewSet(viewsets.ModelViewSet):

    queryset= Servidor.objects.all()
    serializer_class = ServidorSerializer