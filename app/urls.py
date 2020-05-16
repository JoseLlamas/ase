from django.urls import path
from django.views.generic import TemplateView
from .views import Login

app_name = 'app'
urlpatterns = [
    path('', TemplateView.as_view(template_name='app/home.html'), name='home'),
    path('login', Login.as_view(), name='login')
]
