from rest_framework import serializers, viewsets
from app.models import UsuarioMaquina

class UsuarioMaquinaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = UsuarioMaquina
        fields = ['id', 'usuario', 'password', 'activo']

class UsuarioMaquinaViewSet(viewsets.ModelViewSet):

    queryset = UsuarioMaquina.objects.all()
    serializer_class = UsuarioMaquinaSerializer
