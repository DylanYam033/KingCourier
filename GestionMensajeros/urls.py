from django.urls import path
from . import views

# urls propias de la app, por cada view hay una url que contiene la ruta donde esta el html y si no hay se pone solo el nombre en cuestion
urlpatterns = [
    path("", views.mensajero, name="mensajeros"),
    path("create", views.create_mensajero, name="create_mensajeros"),
    path('mensajeros/mensajero/<int:mensajero_id>/', views.detalle_mensajero, name='detalle_mensajero'),
    path('mensajeros/mensajero/<int:mensajero_id>/editar/', views.editar_mensajero, name='editar_mensajero'),
    path('mensajeros/mensajero/<int:mensajero_id>/eliminar/',views.eliminar_mensajero, name='eliminar_mensajero'),
]
