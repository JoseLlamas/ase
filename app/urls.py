from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    APIMaquinaDetailView, 
    APIMaquinaView,
    APIIpView,
    APIIpDetailView,
    APIUsuarioMaquinaView,
    APIUsuarioMaquinaDetailView
)

app_name:str = 'app'

urlpatterns = format_suffix_patterns([
        path('maquina/<int:id>', APIMaquinaDetailView.as_view(), name="maquina-detail"),
        path('maquina/', APIMaquinaView.as_view(), name="maquina-list"),
        path('ip/<int:id>', APIIpDetailView.as_view(), name="ip-detail"),
        path('ip/', APIIpView.as_view(), name="ip-list"),
        path('usuario_maquina/<int:id>', APIUsuarioMaquinaDetailView.as_view(), name='usuario-maquina-detail'),
        path('usuario_maquina/', APIUsuarioMaquinaView.as_view(), name='usuario-maquina-list')
    ])
