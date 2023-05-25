from django import forms
from .models import Pedido, EstadoPedido
from GestionClientes.models import Sucursale, DetalleClienteMensajeros
# from GestionMensajeros.models import Mensajeros

class PedidoForm(forms.ModelForm):
    estado = forms.ModelChoiceField(queryset=EstadoPedido.objects.all(), initial=EstadoPedido.objects.get(nombre='Pendiente'))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PedidoForm, self).__init__(*args, **kwargs)
        if user:
            cliente = user.propietario_cliente
            self.fields['id_cliente'].initial = cliente
            self.fields['id_sucursal_origen'].queryset = Sucursale.objects.filter(cliente=cliente)
            self.fields['id_sucursal_destino'].queryset = Sucursale.objects.filter(cliente=cliente)
            self.fields['id_mensajero'].queryset = DetalleClienteMensajeros.objects.filter(cliente=cliente)

    def clean_id_mensajero(self):
        id_mensajero = self.cleaned_data['id_mensajero']
        if isinstance(id_mensajero, DetalleClienteMensajeros):
            id_mensajero = id_mensajero.mensajero
        return id_mensajero

    class Meta:
        model = Pedido
        fields = ['id_cliente', 'id_mensajero', 'id_sucursal_origen', 'id_sucursal_destino', 'descripcion', 'tipo_trasnporte', 'numero_paquetes', 'estado']