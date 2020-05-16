from rest_framework import serializers, viewsets
from app.models import Ip

class IpSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ip
        fields = ['id', 'ip', 'interfaz', 'mac']


class IpViewSet(viewsets.ModelViewSet):

    queryset = Ip.objects.all()
    serializer_class = IpSerializer
    