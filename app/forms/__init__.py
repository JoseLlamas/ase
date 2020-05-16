from django import forms

class FormLogin(forms.Form):

    usuario = forms.CharField(required=True, error_messages={'required': 'El usuario es requerido'})
    password = forms.CharField(required=True, error_messages={'required': 'La contraseña es requerido'})