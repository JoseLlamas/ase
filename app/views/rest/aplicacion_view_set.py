from rest_framework import serializers, viewsets
from app.models import Aplicacion

class AplicacionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Aplicacion
        fields = [
            'id',
            'nombre',
            'ruta_web',
            'version',
            'repositorio',
            'activo'
        ]

class AplicationViewSet(viewsets.ModelViewSet):

    queryset = Aplicacion.objects.all()
    serializer_class = AplicacionSerializer