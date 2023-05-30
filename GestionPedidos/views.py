from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Pedido, DetalleEstadoPedido, EstadoPedido
from user.models import User
from django.db.models import Max, Subquery, OuterRef
from itertools import zip_longest
from .forms import PedidoForm
from datetime import datetime


# Create your views here.

# listar pedidos de un pedido
@login_required
def pedido(request):
    try:
        pedido = request.user.propietario_cliente
        pedidos = Pedido.objects.filter(id_cliente=pedido)
        
        # Obtener la subconsulta para obtener la fecha_hora máxima para cada pedido del pedido
        subquery = DetalleEstadoPedido.objects.filter(id_pedido__id_cliente_id=pedido).values('id_pedido').annotate(max_fecha_hora=Max('fecha_hora')).values('max_fecha_hora')

        # Obtener los detalles de estado de pedido más recientes para cada pedido del pedido
        detalles = DetalleEstadoPedido.objects.filter(
            id_pedido__id_cliente_id=pedido,
            fecha_hora__in=Subquery(subquery)
        )

        listas_combinadas = zip_longest(pedidos, detalles)

        if pedidos.exists():
            return render(request, 'pedidos/index.html', {'listas_combinadas': listas_combinadas})
        else:
            message = "No hay pedidos registrados"
            return render(request, 'pedidos/index.html', {'message': message})
    except User.DoesNotExist:
        message = "No eres propietario de ningún pedido"
        return render(request, 'pedidos/index.html', {'message': message})


def create_pedido(request):
    error_message = ''  # Inicializar la variable con un valor predeterminado
    if request.method == 'POST':
        form = PedidoForm(request.POST, user=request.user)
        try:
            if form.is_valid():
                form.save()
                return redirect('pedidos')
        except Exception as e:
            # Manejo del error, por ejemplo, mostrar un mensaje de error o realizar alguna acción adicional
            error_message = str(e)
            form.add_error(None, error_message)
    else:
        form = PedidoForm(user=request.user, initial={'fecha_hora': datetime.now()})
    
    return render(request, 'pedidos/create.html', {'form': form, 'error_message': error_message})


def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    return render(request, 'pedidos/detail.html', {
        'pedido': pedido,
    })

def cancelar_pedido(request, pedido_id):
    # Obtener el pedido existente
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    # Obtener el estado con la llave primaria 5
    estado = get_object_or_404(EstadoPedido, pk=5)
    # Crear un nuevo DetalleEstadoPedido
    nuevo_estado_pedido = DetalleEstadoPedido.objects.create(
        id_estado=estado,
        id_pedido=pedido,
        fecha_hora=datetime.now(),  # Establece la fecha y hora actual
    )
    nuevo_estado_pedido.save()
    return redirect('pedidos')