from rest_framework import serializers, viewsets
from app.models import Maquina

class MaquinaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Maquina
        fields = ['id', 'sistema_operativo', 'nombre', 'activo', 'tipo']


class MaquinaViewSet(viewsets.ModelViewSet):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer