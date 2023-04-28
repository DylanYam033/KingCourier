from django.db import models

# Create your models here.


class Mensajeros(models.Model):
    identificacion = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    vehiculo = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
