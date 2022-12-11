from django.shortcuts import render, redirect
from .forms import Login_form, Sign_up_form
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Card
from django.views import View

def login_user(request):
    if request.method == "POST":
        form = Login_form(request.POST)
        user = authenticate(request=request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect("/home")
        else:
            form = Login_form()
    elif request.method == "GET":
        form = Login_form()

    return render(request, "login.html", {"form":form})


@login_required(redirect_field_name='login')
def add_user(request):
    created = False
    name = ""
    if request.method == "POST":
        form = Sign_up_form(request.POST)
        user = User.objects.create_user(request.POST['username'], request.POST['password1'], request.POST['password2'])
        if user is not None and request.POST['password1'] == request.POST['password2'] and User.objects.get(username=request.POST['username']):
            user.save()
            created = True
            name = request.POST['username']
        else:
            form = Sign_up_form()
    elif request.method == "GET":
        form = Sign_up_form()

    return render(request, "add_user.html", {"form":form, "created":created, "name":name})   


def home(request): 
    return render(request, "base.html")   


def logout_user(request):
    logout(request)
    return redirect('/login')


@login_required(redirect_field_name='login')
def workspace(request):
    if request.method == "POST":
        title = request.POST.get("title")
        creator = request.POST.get("creator")
        date = request.POST.get("date")
        cards = Card.objects.all()
        if title != '':
            cards = cards.filter(title=title)
        if creator != '':
            cards = cards.filter(user=User.objects.get(username=creator))
        if date != '':
            cards = cards.filter(create_date=date)
    else:
        cards = Card.objects.all()
    context = {
        'cards':cards
    }

    return render(request, "workspace.html", context)
