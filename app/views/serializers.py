from rest_framework import serializers

class MaquinaSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    sistema_operativo = serializers.CharField(required=True, max_length=100)
    nombre = serializers.CharField(required=True, max_length=30)
    activo = serializers.BooleanField(required=True)
    tipo = serializers.CharField(required=True, max_length=1)