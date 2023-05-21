from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Pedido, DetalleEstadoPedido
from user.models import User
from django.db.models import Max, Subquery, OuterRef
from itertools import zip_longest

# Create your views here.

# listar pedidos de un cliente
@login_required
def pedido(request):
    try:
        cliente = request.user.propietario_cliente
        pedidos = Pedido.objects.filter(id_cliente=cliente)
        
        # Obtener la subconsulta para obtener la fecha_hora máxima para cada pedido del cliente
        subquery = DetalleEstadoPedido.objects.filter(id_pedido__id_cliente_id=cliente).values('id_pedido').annotate(max_fecha_hora=Max('fecha_hora')).values('max_fecha_hora')

        # Obtener los detalles de estado de pedido más recientes para cada pedido del cliente
        detalles = DetalleEstadoPedido.objects.filter(
            id_pedido__id_cliente_id=cliente,
            fecha_hora__in=Subquery(subquery)
        )

        listas_combinadas = zip_longest(pedidos, detalles)

        if pedidos.exists():
            return render(request, 'pedidos/index.html', {'listas_combinadas': listas_combinadas})
        else:
            message = "No hay pedidos registrados"
            return render(request, 'pedidos/index.html', {'message': message})
    except User.DoesNotExist:
        message = "No eres propietario de ningún cliente"
        return render(request, 'pedidos/index.html', {'message': message})

