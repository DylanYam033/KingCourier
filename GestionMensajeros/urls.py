from django.urls import path
from . import views

# urls propias de la app, por cada view hay una url que contiene la ruta donde esta el html y si no hay se pone solo el nombre en cuestion
urlpatterns = [
    path("", views.mensajero, name="mensajeros"),
]
