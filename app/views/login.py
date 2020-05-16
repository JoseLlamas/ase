from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import get_template
from django.contrib.auth.mixins import UserPassesTestMixin
from app.forms import FormLogin

class Login(UserPassesTestMixin, View):

    def test_func(self):
        return True

    def get(self, request:HttpRequest)-> HttpResponse:
        form = FormLogin()
        return HttpResponse(
            get_template('app/login.html').render({'form': form}, request), 
            content_type='text/html;charset=UTF-8'
        )

    def post(self, request:HttpRequest)-> HttpResponse:
        form = FormLogin(request.POST)
        if not form.is_valid():
            return HttpResponse(
                get_template('app/login.html').render({'form': form}, request),
                content_type='text/html;charset=UTF-8'
            )
        else:
            return HttpResponseRedirect(reverse('app:home'))