from django.http import Http404
from django.db import transaction
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    MaquinaSerializer, 
    IpSerializer, 
    IpSerializerUpdate, 
    UsuarioMaquinaSerializer, 
    UsuarioMaquinaUpdateSerializer
)
from app.models import Maquina, Ip, UsuarioMaquina


class APIMaquinaDetailView(APIView):

    def _get_object(self, id:int):
        try:
            return Maquina.objects.get(pk=id)
        except Maquina.DoesNotExist:
            raise Http404

    def get(self, request, id:int):
        maquina = self._get_object(id)
        serializer = MaquinaSerializer(maquina)
        return Response(serializer.data)

    def put(self, request, id:int):
        maquina = self._get_object(id)
        serializer = MaquinaSerializer(maquina, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            with transaction.atomic():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, id:int):
        maquina = self._get_object(id)
        with transaction.atomic():
            for ip in maquina.ips.all():
                ip.activo = False
                ip.save()
            for usuario in maquina.usuarios.all():
                usuario.activo = False
                usuario.save()
            maquina.activo = False
            maquina.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class APIMaquinaView(APIView):

    def get(self, request):
        serializer = MaquinaSerializer(Maquina.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MaquinaSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            with transaction.atomic():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class APIIpDetailView(APIView):

    def _get_object(self, id):
        try:
            return Ip.objects.get(pk=id)
        except Ip.DoesNotExist:
            raise Http404

    def get(self, request, id:int):
        ip = self._get_object(id)
        return Response(IpSerializer(ip).data)

    def put(self, request, id:int):
        ip = self._get_object(id)
        serializer = IpSerializerUpdate(ip, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            with transaction.atomic():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, id:int):
        ip = self._get_object(id)
        with transaction.atomic():
            ip.activo = False
            ip.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class APIIpView(APIView):

    def get(self, request):
        serializer = IpSerializer(Ip.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IpSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            with transaction.atomic():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class APIUsuarioMaquinaDetailView(APIView):

    def _get_object(self, id):
        try:
            return UsuarioMaquina.objects.get(pk=id)
        except UsuarioMaquina.DoesNotExist:
            raise Http404

    def get(self, request, id):
        serializer = UsuarioMaquinaSerializer(self._get_object(id))
        return Response(serializer.data)

    def put(self, request, id):
        serializer = UsuarioMaquinaUpdateSerializer(self._get_object(id), data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            with transaction.atomic():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, id):
        usuario_maquina = self._get_object(id)
        with transaction.atomic():
            usuario_maquina.activo = False
            usuario_maquina.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class APIUsuarioMaquinaView(APIView):

    def get(self, request):
        serializer = UsuarioMaquinaSerializer(UsuarioMaquina.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioMaquinaSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            with transaction.atomic():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

