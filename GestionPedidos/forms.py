from django import forms
from .models import Pedido, EstadoPedido, DetalleEstadoPedido
from GestionClientes.models import Sucursale, DetalleClienteMensajeros
# from GestionMensajeros.models import Mensajeros
from django.utils import timezone

class PedidoForm(forms.ModelForm):
    estado = forms.ModelChoiceField(queryset=EstadoPedido.objects.all(), initial=EstadoPedido.objects.get(nombre='Solicitado'), widget=forms.HiddenInput())

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

    def save(self, commit=True):
        pedido = super().save(commit=False)
        fecha_hora = timezone.now()
        estado = EstadoPedido.objects.get(nombre='Solicitado')  # Obtener la instancia de EstadoPedido
        if commit:
            pedido.save()
            DetalleEstadoPedido.objects.create(id_pedido=pedido, id_estado=estado, fecha_hora=fecha_hora)
        return pedido

    class Meta:
        model = Pedido
        fields = ['id_cliente', 'id_mensajero', 'id_sucursal_origen', 'id_sucursal_destino', 'descripcion', 'tipo_trasnporte', 'numero_paquetes','estado']