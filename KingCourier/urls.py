from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("login.urls")),
    path('clientes/', include("GestionClientes.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('mensajeros/', include("GestionMensajeros.urls")),
]
