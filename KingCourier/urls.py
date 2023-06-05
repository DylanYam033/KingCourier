from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("login.urls")),
    path('', include("GestionClientes.urls")),
    path('welcome/', TemplateView.as_view(template_name='welcome.html'), name='welcome'),
    path('mensajeros/', include("GestionMensajeros.urls")),
    path('pedidos/', include("GestionPedidos.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
