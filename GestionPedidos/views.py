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
        cliente = request.user.propietario_cliente

        # Obtener la subconsulta para obtener la fecha_hora máxima para cada pedido del pedido
        subquery = DetalleEstadoPedido.objects.filter(id_pedido__id_cliente_id=cliente).values(
            'id_pedido').annotate(max_fecha_hora=Max('fecha_hora')).values('max_fecha_hora')

        # Obtener los detalles de estado de pedido más recientes para cada pedido del pedido
        detalles = DetalleEstadoPedido.objects.filter(
            id_pedido__id_cliente_id=cliente,
            fecha_hora__in=Subquery(subquery)
        )

        if detalles.exists():
            return render(request, 'pedidos/index.html', {'detalles': detalles})
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
        form = PedidoForm(user=request.user, initial={
                          'fecha_hora': datetime.now()})

    return render(request, 'pedidos/create.html', {'form': form, 'error_message': error_message})


def detalle_pedido(request, pedido_id):
    # Obtener el último registro del detalle del pedido
    ultimo_detalle = DetalleEstadoPedido.objects.filter(id_pedido=pedido_id).latest('fecha_hora')

    # Renderizar la plantilla con el detalle del pedido
    return render(request, 'pedidos/detail.html', {
        'pedido': ultimo_detalle,
    })

def cancelar_pedido(request, pedido_id):
    # Obtener el pedido existente
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    # Obtener el estado cancelado por medio de su id
    estado = get_object_or_404(EstadoPedido, pk=6)
    # Crear un nuevo DetalleEstadoPedido
    nuevo_estado_pedido = DetalleEstadoPedido.objects.create(
        id_estado=estado,
        id_pedido=pedido,
        fecha_hora=datetime.now(),  # Establece la fecha y hora actual
    )
    nuevo_estado_pedido.save()
    return redirect('pedidos')


def pedido_mensajero(request):
    try:
        mensajero = request.user.propietario_mensajero

        # Obtener la subconsulta para obtener la fecha_hora máxima para cada pedido del pedido
        subquery = DetalleEstadoPedido.objects.filter(id_pedido__id_mensajero_id=mensajero).values(
            'id_pedido').annotate(max_fecha_hora=Max('fecha_hora')).values('max_fecha_hora')

        # Obtener los detalles de estado de pedido más recientes para cada pedido del pedido
        detalles = DetalleEstadoPedido.objects.filter(
            id_pedido__id_mensajero_id=mensajero,
            fecha_hora__in=Subquery(subquery)
        )

        if detalles.exists():
            return render(request, 'pedidos/mensajeroPedidos.html', {'detalles': detalles})
        else:
            message = "No hay pedidos registrados"
            return render(request, 'pedidos/mensajeroPedidos.html', {'message': message})
    except User.DoesNotExist:
        message = "No eres propietario de ningún pedido"
        return render(request, 'pedidos/mensajeroPedidos.html', {'message': message})


def cambiar_estado_pedido(request, pedido_id):
    # Obtener el pedido existente
    pedido = get_object_or_404(Pedido, pk=pedido_id)

    # Obtener todos los estados de pedido disponibles
    estados = EstadoPedido.objects.all()

    if request.method == 'POST':
        # Obtener el ID del estado seleccionado desde el formulario del template
        id_estado_seleccionado = request.POST.get('estado_seleccionado')

        # Obtener el estado seleccionado por medio de su ID
        estado_seleccionado = get_object_or_404(
            EstadoPedido, pk=id_estado_seleccionado)

        # Crear un nuevo DetalleEstadoPedido
        nuevo_estado_pedido = DetalleEstadoPedido.objects.create(
            id_estado=estado_seleccionado,
            id_pedido=pedido,
            fecha_hora=datetime.now(),  # Establecer la fecha y hora actual
        )

        # Obtener el archivo de imagen enviado
        foto = request.FILES.get('foto')
        if foto:
            nuevo_estado_pedido.foto = foto

        nuevo_estado_pedido.save()
        return redirect('mensajero_pedidos')

    # Renderizar el template con los estados y el pedido
    return render(request, 'pedidos/cambiar_estado.html', {'estados': estados, 'pedido': pedido})


def reporte_pedidos_cliente(request):
    # Obtener todos los pedidos
    pedidos = Pedido.objects.all()
    return render(request, 'reportes/reportes_cliente.html', {'pedidos': pedidos})

def reporte_pedidos_fecha(request):
    # Obtener todos los pedidos
    pedidos = Pedido.objects.all()
    return render(request, 'reportes/reportes_mes.html', {'pedidos': pedidos})

def reporte_pedidos_mensajero(request):
    # Obtener todos los pedidos
    pedidos = Pedido.objects.all()
    return render(request, 'reportes/reportes_mensajero.html', {'pedidos': pedidos})

