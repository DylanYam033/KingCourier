from django.urls import path
from . import views

urlpatterns = [
    path("", views.pedido, name="pedidos"),
    path("create/", views.create_pedido, name="create_pedido"),
    path('pedidos/pedido/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
    path('pedidos/pedido/<int:pedido_id>/cancelar', views.cancelar_pedido, name='cancelar_pedido'),
    path('mensajero_pedidos/', views.pedido_mensajero, name='mensajero_pedidos'),
    path('pedidos/pedido/<int:pedido_id>/cambiar_estado', views.cambiar_estado_pedido, name='cambiar_estado_pedido'),
    path("reporte/", views.reporte_pedidos_cliente, name="reporte_pedido_cliente"),
    path("reporte_fecha/", views.reporte_pedidos_fecha, name="reporte_pedido_fecha"),
    path("reporte_mensajero/", views.reporte_pedidos_mensajero, name="reporte_pedido_mensajero"),
    path("reporte_mensajero_pdf/", views.ListPedidos_mensajeroPdf.as_view(), name="reporte_pedido_mensajero_pdf"),
    path("reporte_meses_pdf/", views.ListPedidos_mesesPdf.as_view(), name="reporte_pedido_meses_pdf"),
    path("reporte_clientes_pdf/", views.ListPedidos_clientesPdf.as_view(), name="reporte_pedido_clientes_pdf"),
]
