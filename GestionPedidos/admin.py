from django.contrib import admin
from .models import Pedido, DetalleEstadoPedido, EstadoPedido

# Register your models here.
admin.site.register(Pedido)
admin.site.register(DetalleEstadoPedido)
admin.site.register(EstadoPedido)