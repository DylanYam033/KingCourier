from django.db import models
from GestionMensajeros.models import Mensajeros
# Create your models here.


class Cliente(models.Model):
    identificacion = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    mensajeros = models.ManyToManyField(Mensajeros)

    def __str__(self):
        return self.nombre


class Sucursale(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

