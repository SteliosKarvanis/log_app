from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.login),
    path('home', views.home),
    path('login', views.login, name='login'),
    path('login/sign_up', lambda req: redirect('/sign_up')),
    path('login/login', lambda req: redirect('/login')),
    path('sign_up', views.sign_up, name='sign_up'),
]
