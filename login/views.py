from django.shortcuts import render, redirect
# crea una cookie de autenticacion
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import UserForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def perfil(request):
    return render(request, 'perfil.html')


def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')

    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        print(request.POST)
        print(user)
        if user is None:
            return render(request, 'home.html', {
                'error': 'username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('perfil')

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('perfil')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


@login_required
def log_out(request):
    logout(request)
    return redirect('login')
