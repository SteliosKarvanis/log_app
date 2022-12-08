from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.set_user),
    path('home', views.home),
    path('login', views.set_user, name='login'),
    path('login/add_user', lambda req: redirect('/add_user')),
    path('login/login', lambda req: redirect('/login')),
    path('add_user', views.add_user, name='add_user'),
    path('logout_user', views.logout_user),
]
