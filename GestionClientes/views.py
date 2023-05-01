from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Sucursale
from .forms import CreateCliente, SucursaleForm
from django.contrib.auth.decorators import login_required
from user.models import User

# Create your views here.

# listar clientes registrados
@login_required
def cliente(request):
    cliente = Cliente.objects.filter(activo=True)
    if cliente.exists():
        return render(request, 'clientes/index.html', {
            'clientes': cliente
        })
    else:
        message = "No hay clientes registrados"
        return render(request, 'clientes/index.html', {
            'message': message
        })

# crear clientes


def create_cliente(request):
    if request.method == 'GET':
        return render(request, 'clientes/create.html', {
            'createForm': CreateCliente()
        })
    else:
        data = CreateCliente(request.POST)
        if data.is_valid():
            # Agrega una validación personalizada para la identificación
            identificacion = data.cleaned_data['identificacion']
            if Cliente.objects.filter(identificacion=identificacion).exists():
                return render(request, 'clientes/create.html', {
                    'createForm': data,
                    'error': 'La identificación ya existe'
                })

            new_cliente = data.save(commit=False)
            new_cliente.user = request.user
            new_cliente.save()
            return redirect('clientes')
        else:
            return render(request, 'clientes/create.html', {
                'createForm': data,
                'error': 'Datos inválidos'
            })


# detalles de un cliente
def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    # Filtrar los usuarios cuyo propietario cliente sea igual al del detalle
    users = User.objects.filter(propietario_cliente=cliente_id)
    # Filtrar las sucursales cuyo cliente sea igual al del detalle
    sucursales = Sucursale.objects.filter(cliente=cliente_id)
    return render(request, 'clientes/detail.html', {
        'cliente': cliente,
        'users': users,
        'sucursales': sucursales,
    })

# editar cliente
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        form = CreateCliente(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('detalle_cliente', cliente_id=cliente.id)
    else:
        form = CreateCliente(instance=cliente)
    return render(request, 'clientes/edit.html', {
        'form': form, 'cliente': cliente
    })

# eliminar cliente


def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    cliente.activo = False
    cliente.save()
    return redirect('clientes')


# listar sucursales registradas
def sucursal(request):
    sucursal = Sucursale.objects.filter(cliente=request.user.propietario_cliente)
    if sucursal.exists():
        return render(request, 'sucursales/index.html', {
            'sucursales': sucursal
        })
    else:
        message = "No hay clientes registrados"
        return render(request, 'sucursales/index.html', {
            'message': message
        })


from django.shortcuts import render, redirect
from .forms import SucursaleForm

def create_sucursal(request):
    if request.method == 'POST':
        form = SucursaleForm(request.POST, user=request.user)
        if form.is_valid():
            new_sucursal = form.save(commit=False)
            new_sucursal.cliente = request.user.propietario_cliente
            new_sucursal.save()
            return redirect('sucursales')
    else:
        form = SucursaleForm(user=request.user)
    return render(request, 'sucursales/create.html', {
        'form': form}
        )



def detalle_sucursal(request, sucursal_id):
    sucursal = get_object_or_404(Sucursale, pk=sucursal_id)
    return render(request, 'sucursales/detail.html', {
        'sucursal': sucursal
    })

# editar cliente
def editar_sucursal(request, sucursal_id):
    sucursal = get_object_or_404(Sucursale, pk=sucursal_id)
    if request.method == 'POST':
        form = SucursaleForm(request.POST, instance=sucursal)
        if form.is_valid():
            form.save()
            return redirect('detalle_sucursal', sucursal_id=sucursal.id)
    else:
        form = SucursaleForm(instance=sucursal)
    return render(request, 'sucursales/edit.html', {
        'form': form, 'sucursal': sucursal
    })


def eliminar_sucursal(request, sucursal_id):
    sucursal = get_object_or_404(Sucursale, pk=sucursal_id)
    sucursal.activo = False
    sucursal.save()
    return redirect('sucursales')


#listar cuentas de un cliente
@login_required
def accouns_clients(request):
    # Obtener el propietario cliente del usuario en sesión
    propietario_cliente_buscar = request.user.propietario_cliente
    # Filtrar los usuarios cuyo propietario cliente sea igual al del usuario en sesión
    users = []
    if (propietario_cliente_buscar != None):
        users = User.objects.filter(propietario_cliente=propietario_cliente_buscar)
    if users:
        # Si hay usuarios, los mostramos
        return render(request, 'clientes/accounts.html', {
            'users': users
        })
    else:
        # Si no hay usuarios, mostramos un mensaje
        message = "No hay usuarios aún"
        return render(request, 'clientes/accounts.html', {
            'message': message
        })

