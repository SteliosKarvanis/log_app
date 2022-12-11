from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.login_user),
    path('login', views.login_user, name='login'),
    path('login/add_user', lambda req: redirect('/add_user')),
    path('login/login', lambda req: redirect('/login')),
    path('add_user', views.add_user, name='add_user'),
    path('logout_user', views.logout_user),
    path('add_card', views.create_card),
    path('workspace', views.workspace)
]
