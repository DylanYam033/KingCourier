from django.shortcuts import render, redirect, get_object_or_404
from .models import Mensajeros


# Create your views here.

# listar mensajeros registrados


def mensajero(request):
    mensajero = Mensajeros.objects.filter(activo=True)
    if mensajero.exists():
        return render(request, 'mensajeros/index.html', {
            'mensajeros': mensajero
        })
    else:
        message = "No hay mensajeros registrados"
        return render(request, 'mensajeros/index.html', {
            'message': message
        })
