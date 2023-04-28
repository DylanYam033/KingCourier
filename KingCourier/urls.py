from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("login.urls")),
    # path('accounts/', include("django.contrib.auth.urls")),
    path('clientes/', include("GestionClientes.urls")),
    path('mensajeros/', include("GestionMensajeros.urls")),
    path('bienvenida/', TemplateView.as_view(template_name='welcome.html'), name='welcome'),
]
