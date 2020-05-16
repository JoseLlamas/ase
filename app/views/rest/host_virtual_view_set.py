from rest_framework import serializers, viewsets
from app.models import HostVirtual

class HostVirtualSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = HostVirtual
        fields = ['id', 'nombre', 'puerto', 'default']


class HostVirtualViewSet(viewsets.ModelViewSet):

    queryset = HostVirtual.objects.all()
    serializer_class = HostVirtualSerializer