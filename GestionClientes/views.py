from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Sucursale
from .forms import CreateCliente, SucursaleForm
from django.contrib.auth.decorators import login_required, user_passes_test
from user.models import User

# Create your views here.

# listar clientes registrados
@login_required
@user_passes_test(lambda user: user.is_superuser)
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

@user_passes_test(lambda user: user.is_superuser)
@login_required
def create_cliente(request):
    if request.method == 'GET':
        form = CreateCliente()
        return render(request, 'clientes/create.html', {'createForm': form})
    else:
        form = CreateCliente(request.POST)
        if form.is_valid():
            identificacion = form.cleaned_data['identificacion']
            if Cliente.objects.filter(identificacion=identificacion).exists():
                return render(request, 'clientes/create.html', {
                    'createForm': form,
                    'error': 'La identificación ya existe'
                })

            selected_mensajeros = request.POST.getlist('mensajeros')
            new_cliente = form.save(commit=False)
            new_cliente.user = request.user
            new_cliente.save()
            new_cliente.mensajeros.set(selected_mensajeros)
            return redirect('clientes')
        else:
            return render(request, 'clientes/create.html', {
                'createForm': form,
                'error': 'Datos inválidos'
            })


# detalles de un cliente
@user_passes_test(lambda user: user.is_superuser)
@login_required
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
@user_passes_test(lambda user: user.is_superuser)
@login_required
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

@user_passes_test(lambda user: user.is_superuser)
@login_required
def eliminar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.activo = False
    cliente.save()
    return redirect('clientes')


# listar sucursales registradas
@login_required
def sucursal(request):
    sucursal = Sucursale.objects.filter(cliente=request.user.propietario_cliente, activo=True)
    if sucursal.exists():
        return render(request, 'sucursales/index.html', {
            'sucursales': sucursal
        })
    else:
        message = "No hay sucursales registradas"
        return render(request, 'sucursales/index.html', {
            'message': message
        })

@login_required
def create_sucursal(request):
    cliente = request.user.propietario_cliente
    if request.method == 'GET':
        return render(request, 'sucursales/create.html', {
            'createForm': SucursaleForm(),
            'cliente': cliente
        })
    else:
        data = SucursaleForm(request.POST)
        print(data)
        if data.is_valid():
            new_sucursal = data.save(commit=False)
            new_sucursal.cliente = cliente
            new_sucursal.save()
            return redirect('sucursales')
        else:
            return render(request, 'sucursales/create.html', {
                'createForm': data,
                'cliente': cliente,
                'error': 'Datos inválidos',
            })


@login_required
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

@login_required
def eliminar_sucursal(request, sucursal_id):
    sucursal = Sucursale.objects.get(id=sucursal_id)
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

