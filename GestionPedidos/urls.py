from django.urls import path
from . import views

urlpatterns = [
    path("", views.pedido, name="pedidos"),
    path("create/", views.create_pedido, name="create_pedido"),
    
]
