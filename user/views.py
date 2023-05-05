from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from .models import User


# Create your views here.
@login_required
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('users')
    else:
        form = UserForm()
    return render(request, 'login/register.html', {'form': form})

@login_required
def users_list(request):
    users = User.objects.exclude(is_superuser=True)
    if users.exists():
        return render(request, 'login/users.html', {
            'users': users
        })
    else:
        message = "No hay Usuarios Registrados"
        return render(request, 'login/users.html', {
            'message': message
        })

def edit_profile(request):
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserForm(instance=request.user)
    return render(request, 'login/edit_profile.html', {
        'form': form
        })