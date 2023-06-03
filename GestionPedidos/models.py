from django.db import models
from GestionMensajeros.models import Mensajeros
from GestionClientes.models import Cliente, Sucursale
# Create your models here.


class Pedido(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_mensajero = models.ForeignKey(Mensajeros, on_delete=models.CASCADE)
    id_sucursal_origen = models.ForeignKey(Sucursale, on_delete=models.CASCADE, related_name='sucursal_origen')
    id_sucursal_destino = models.ForeignKey(Sucursale, on_delete=models.CASCADE, related_name='sucursal_destino')
    descripcion = models.CharField(max_length=100)
    tipo_trasnporte = models.CharField(max_length=20)
    numero_paquetes = models.CharField(max_length=100)
   
    def __str__(self):
        return str(self.id_cliente) + " - " + str(self.id_mensajero)
    
class EstadoPedido(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class DetalleEstadoPedido(models.Model):
    id_estado = models.ForeignKey(EstadoPedido, on_delete=models.CASCADE)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now=False, auto_now_add=False)
    foto = models.ImageField(upload_to='detalles_estado', null=True, blank=True)
    def __str__(self):
        return str(self.id_estado)+ " - " + str(self.id_pedido)