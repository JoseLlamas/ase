from rest_framework import serializers
from app.models import Maquina
from app.models import Ip
from app.models import UsuarioMaquina
from app.models import Servidor
from app.models import Aplicacion
from app.models import HostVirtual
from app.models import Aplicacion

####serializers para modelos Ip
class _IpSerializerMetaMixim():

    model = Ip
    fields = ['id', 'ip', 'interfaz', 'mac', 'activo', 'nombre_maquina', 'maquina', 'created_at']


class IpSerializer(serializers.ModelSerializer):

    nombre_maquina = serializers.ReadOnlyField(source='maquina.nombre')

    class Meta(_IpSerializerMetaMixim):
        read_only_fields = ['created_at']


class IpSerializerUpdate(serializers.ModelSerializer):

    nombre_maquina = serializers.ReadOnlyField(source='maquina.nombre')

    class Meta(_IpSerializerMetaMixim):
        read_only_fields = ['ip', 'created_at', 'activo', 'maquina']
#########################

######serializers para modelo UsuarioMaquina
class UsuarioMaquinaSerializer(serializers.ModelSerializer):

    class Meta:

        model = UsuarioMaquina
        fields = ['id', 'usuario', 'password', 'maquina', 'activo', 'created_at']
        read_only_fields = ['created_at']


class UsuarioMaquinaUpdateSerializer(serializers.ModelSerializer):


    class Meta:

        model = UsuarioMaquina
        fields = ['id', 'usuario', 'password', 'maquina', 'activo', 'created_at']
        read_only_fields = ['created_at', 'maquina', 'activo']

############################

######serializers Para Maquina
class MaquinaSerializer(serializers.ModelSerializer):

    class IpSerializer(serializers.ModelSerializer):

        class Meta:
            model = Ip
            fields = ['id', 'ip', 'interfaz', 'mac', 'activo', 'created_at']
            read_only_fields = ['created_at']

    ips = IpSerializer(many=True, required=False)

    class UsuarioMaquinaSerializer(serializers.ModelSerializer):

        class Meta:
            model = UsuarioMaquina
            fields = ['id', 'usuario', 'password', 'activo', 'created_at']
            read_only_fields = ['created_at']

    usuarios = UsuarioMaquinaSerializer(many=True, required=False)

    class Meta:

        model = Maquina
        fields = ['id', 'sistema_operativo', 'nombre', 'activo', 'tipo', 'created_at', 'ips', 'usuarios']

    def create(self, validate_data):
        data_ips = validate_data.pop('ips', None)
        data_usuario_maquinas = validate_data.pop('usuarios', None)
        maquina = Maquina.objects.create(**validate_data)
        if data_ips is not None:
            for data_ip in data_ips:
                Ip.objects.create(maquina=maquina, **data_ip)
        if data_usuario_maquinas is not None:
            for data_usuario_maquina in data_usuario_maquinas:
                UsuarioMaquina.objects.create(maquina=maquina, **data_usuario_maquina)
        return maquina

    def update(self, instance, validate_data):
        instance.sistema_operativo = validate_data.get('sistema_operativo')
        instance.activo = validate_data.get('activo')
        instance.tipo = validate_data.get('tipo')
        instance.nombre = validate_data.get('nombre')
        instance.save()
        return instance

###############serializers para servidores

class ServidorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Servidor
        fields = [
            'id',
            'modo',
            'nombre',
            'version',
            'root_path',
            'puerto_admin',
            'usuario_admin',
            'password_admin',
            'maquina',
            'activo',
            'created_at'
        ]
        read_only_fields = ['created_at', 'activo']


class ServidorUpdateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Servidor
        fields = [
            'id',
            'modo',
            'nombre',
            'version',
            'root_path',
            'puerto_admin',
            'usuario_admin',
            'password_admin',
            'maquina',
            'activo',
            'created_at'
        ]
        read_only_fields = [
            'maquina',
            'activo',
            'created_at'
        ]

##########################

######serializers host-virtual

class HostVirtualSerializer(serializers.ModelSerializer):

    class Meta:

        model = HostVirtual
        fields = [
            'id',
            'nombre',
            'puerto',
            'activo',
            'created_at',
            'servidor',
            'default'
        ]
        read_only_fields = [
            'created_at',
            'default'
        ]

class HostVirtualUpdateSerializer(serializers.ModelSerializer):

    class Meta:

        model = HostVirtual
        fields = [
            'id',
            'nombre',
            'puerto',
            'activo',
            'created_at',
            'servidor'
        ]
        read_only_fields = [
            'created_at',
            'servidor',
            'activo'
        ]


##############

#######serializers aplicaciones########

class AplicacionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Aplicacion
        fields = [
            'nombre',
            'ruta_web',
            'version',
            'repositorio',
            'activo',
            'host_virtual',
            'created_at'
        ]
        read_only_fields = [
            'created_at',
            'activo'
        ]


class AplicacionUpdateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Aplicacion
        fields =  [
            'nombre',
            'ruta_web',
            'version',
            'repositorio',
            'activo',
            'host_virtual'
        ]
        read_only_fields = [
            'created_at',
            'activo',
            'host_virtual'
        ]

