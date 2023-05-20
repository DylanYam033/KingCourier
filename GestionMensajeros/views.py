from django.shortcuts import render, redirect, get_object_or_404
from .models import Mensajeros
from .forms import MensajeroForm
from GestionClientes.models import DetalleClienteMensajeros, Cliente


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

def create_mensajero(request):
    if request.method == 'GET':
        return render(request, 'mensajeros/create.html', {
            'createForm': MensajeroForm()
        })
    else:
        data = MensajeroForm(request.POST)
        print(data)
        if data.is_valid():
            # Agrega una validación personalizada para la identificación
            identificacion = data.cleaned_data['identificacion']
            if Mensajeros.objects.filter(identificacion=identificacion).exists():
                return render(request, 'mensajeros/create.html', {
                    'createForm': data,
                    'error': 'La identificación ya existe'
                })

            new_cliente = data.save(commit=False)
            new_cliente.user = request.user
            new_cliente.save()
            return redirect('mensajeros')
        else:
            return render(request, 'mensajeros/create.html', {
                'createForm': data,
                'error': 'Datos inválidos'
            })
        
def detalle_mensajero(request, mensajero_id):
    # Filtra los clientes cuyo mensajero es igual al del detalle
    detalle_clientes = DetalleClienteMensajeros.objects.filter(mensajero=mensajero_id)
    mensajero = get_object_or_404(Mensajeros, pk=mensajero_id)
    return render(request, 'mensajeros/detail.html', {
        'mensajero': mensajero,
        'detalle_clientes': detalle_clientes
        }
    )

def clientes_mensajero(request):
    try:
        mensajero = request.user.propietario_mensajero
        clientes = Cliente.objects.filter(detalleclientemensajeros__mensajero=mensajero)
        
        if clientes.exists():
            return render(request, 'mensajeros/clientes.html', {
                'clientes': clientes
            })
        else:
            message = "No tiene clientes asociados"
            return render(request, 'sucursales/index.html', {
                'message': message
            })
    except Mensajeros.DoesNotExist:
        message = "No es un mensajero válido"
        return render(request, 'sucursales/index.html', {
            'message': message
        })

    
def editar_mensajero(request, mensajero_id):
    mensajero = get_object_or_404(Mensajeros, pk=mensajero_id)
    if request.method == 'POST':
        form = MensajeroForm(request.POST, instance=mensajero)
        if form.is_valid():
            form.save()
            return redirect('detalle_mensajero', mensajero_id=mensajero.id)
    else:
        form = MensajeroForm(instance=mensajero)
    return render(request, 'mensajeros/edit.html', {
        'form': form, 'mensajero': mensajero
    })


def eliminar_mensajero(request, mensajero_id):
    mensajero = Mensajeros.objects.get(id=mensajero_id)
    mensajero.activo = False
    mensajero.save()
    return redirect('mensajeros')