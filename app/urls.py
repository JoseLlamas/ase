from django.urls import path, include
from rest_framework import routers
from .views.rest import (
    MaquinaViewSet, 
    ServidorViewSet, 
    AplicationViewSet,
    IpViewSet,
    UsuarioMaquinaViewSet,
    HostVirtualViewSet
)

router = routers.DefaultRouter()

router.register('maquina', MaquinaViewSet)
router.register('servidor', ServidorViewSet)
router.register('aplicacion', AplicationViewSet)
router.register('ip', IpViewSet)
router.register('usuario-maquina', UsuarioMaquinaViewSet)
router.register('host-virtual', HostVirtualViewSet)

app_name = 'app'
urlpatterns = [
    path('rest-api/', include(router.urls))
]
