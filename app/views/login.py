from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin
from app.forms import FormLogin

class Login(UserPassesTestMixin, View):

    def test_func(self):
        return True

    def get(self, request:HttpRequest)-> HttpResponse:
        return HttpResponse(
            'hiiii', 
            content_type='text/plain;charset=UTF-8'
        )

    def post(self, request:HttpRequest)-> HttpResponse:
        form = FormLogin(request.POST)
        if not form.is_valid():
            return HttpResponse(
                form.get_json(),
                content_type='application/json'
            )
        else:
            return HttpResponseRedirect(reverse('app:home'))
