from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Pedido
from user.models import User

# Create your views here.

# listar pedidos de un cliente
@login_required
def pedido(request):
    try:
        cliente = request.user.propietario_cliente
        pedidos = Pedido.objects.filter(id_cliente=cliente)
        if pedidos.exists():
            return render(request, 'pedidos/index.html', {'pedidos': pedidos})
        else:
            message = "No hay pedidos registrados"
            return render(request, 'pedidos/index.html', {'message': message})
    except User.DoesNotExist:
        message = "No eres propietario de ningún cliente"
        return render(request, 'pedidos/index.html', {'message': message})

