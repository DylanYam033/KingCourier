from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User


# Create your views here.

@user_passes_test(lambda user: user.is_superuser)
@login_required
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            return redirect('users')
    else:
        form = UserForm()
    return render(request, 'login/register.html', {'form': form})

@user_passes_test(lambda user: user.is_superuser)
@login_required
def users_list(request):
    users = User.objects.exclude(is_superuser=True).filter(is_active=True)
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
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            new_profile_photo = form.cleaned_data.get('profile_photo')
            if new_profile_photo:
                user.profile_photo = new_profile_photo
            form.save()
            return redirect('perfil')
    else:
        form = UserForm(instance=request.user)

    return render(request, 'login/edit_profile.html', {'form': form})

@user_passes_test(lambda user: user.is_superuser)
def eliminar_usuario(request, user_id):
    usuario = User.objects.get(id=user_id)
    usuario.is_active = False
    usuario.save()
    return redirect('users')