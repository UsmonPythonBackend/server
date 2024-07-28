from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout


def cart(request):
    return render(request, 'cart.html')


def xaridlar(request):
    return render(request, 'xaridlar.html')


def users(request):
    return render(request, 'users.html')


def xatolik(request):
    return render(request, 'Xatolik.html')


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request, "auth/login.html", context={'message': 'user not found'})

    return render(request, 'auth/login.html')


def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            return render(request, "auth/register.html", context={'message_password': 'Error Password'})
        else:
            if User.objects.filter(username=username).exists():
                return render(request, 'auth/register.html', context={'message': 'Username already exists'})
            new_user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            return redirect('login')

    return render(request, 'auth/register.html')


def logout_view(request):
    logout(request)
    return redirect('login')