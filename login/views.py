from django.shortcuts import render, redirect
# crea una cookie de autenticacion
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import UserForm
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
=======

>>>>>>> 8257c1e (nuevo comienzo con clientes, sucursales, login y registro de usuarios funcional)
# Create your views here.


def perfil(request):
    return render(request, 'perfil.html')


<<<<<<< HEAD
def login_home(request):
    if request.method == 'GET':
        return render(request, 'login.html')
=======
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
>>>>>>> 8257c1e (nuevo comienzo con clientes, sucursales, login y registro de usuarios funcional)

    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        print(request.POST)
        print(user)
        if user is None:
<<<<<<< HEAD
            return render(request, 'login.html', {
                'error': 'usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('welcome')

=======
            return render(request, 'home.html', {
                'error': 'username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('perfil')
>>>>>>> 8257c1e (nuevo comienzo con clientes, sucursales, login y registro de usuarios funcional)

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('perfil')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


<<<<<<< HEAD
@login_required
def log_out(request):
    logout(request)
    return redirect('home')
=======
>>>>>>> 8257c1e (nuevo comienzo con clientes, sucursales, login y registro de usuarios funcional)
