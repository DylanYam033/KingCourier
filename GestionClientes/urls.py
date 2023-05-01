from django.urls import path
from . import views

# urls propias de la app, por cada view hay una url que contiene la ruta donde esta el html y si no hay se pone solo el nombre en cuestion
urlpatterns = [
    path("clientes/", views.cliente, name="clientes"),
    path("create/", views.create_cliente, name="create_cliente"),
    path('clientes/cliente/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('clientes/cliente/<int:cliente_id>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/cliente/<int:cliente_id>/eliminar/',views.eliminar_cliente, name='eliminar_cliente'),
    path("sucursales/", views.sucursal, name="sucursales"),
    path("sucursales/create/", views.create_sucursal, name="create_sucursal"),
    path('sucursales/sucursal/<int:sucursal_id>/', views.detalle_sucursal, name='detalle_sucursal'),
    path('sucursales/sucursal/<int:sucursal_id>/editar/', views.editar_sucursal, name='editar_sucursal'),
    path('sucursales/sucursal/<int:sucursal_id>/eliminar/', views.eliminar_sucursal, name='eliminar_sucursal'),
    path("accounts/", views.accouns_clients, name="accounts_client"),
]
