from django.urls import path
from . import views

urlpatterns = [
    path("", views.pedido, name="pedidos"),
    path("create/", views.create_pedido, name="create_pedido"),
    path('pedidos/pedido/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
    path('pedidos/pedido/<int:pedido_id>/cancelar', views.cancelar_pedido, name='cancelar_pedido'),
    path('mensajero_pedidos/', views.pedido_mensajero, name='mensajero_pedidos'),
    path('pedidos/pedido/<int:pedido_id>/cambiar_estado', views.cambiar_estado_pedido, name='cambiar_estado_pedido'),
]
