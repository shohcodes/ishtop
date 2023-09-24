from django.contrib import auth
from django.contrib.auth import authenticate, login as _login
from django.contrib.auth.decorators import login_required as _login_required
from django.shortcuts import redirect
from django.shortcuts import render

from users.models import User


def login_required(f):
    return _login_required(f, login_url="registration")


def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            _login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def registration(request):
    if request.POST:
        fullname = request.POST['fullname']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(
            fullname=fullname, phone_number=phone_number,
            email=email, username=username, password=password
        )
        _login(request, user)
        return redirect('index')
    else:
        return render(request, 'registration.html')


@login_required
def index(request):
    context = {}
    return render(request, 'index.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect('registration', )
