from django.shortcuts import render, redirect
from .forms import Login_form, Sign_up_form
from django.contrib.auth import login, logout, authenticate


def login(request):
    if request.method == "POST":
        form = Login_form(request.POST)
    elif request.method == "GET":
        form = Login_form()

    return render(request, "login.html", {"form":form})


def sign_up(request):
    if request.method == "POST":
        form = Sign_up_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    elif request.method == "GET":
        form = Sign_up_form()

    return render(request, "sign_up.html", {"form":form})   

def home(request):
    return render(request, 'base.html')