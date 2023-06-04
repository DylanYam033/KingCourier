from django.db import models
from django.contrib.auth.models import AbstractUser
from GestionClientes import models as modelos_g_clientes
from GestionMensajeros import models as modelos_g_mensajeros

# Create your models here.


class User(AbstractUser):
    num_phone = models.CharField("Telefono", max_length=10)
    address = models.CharField("Direccion", max_length=100)
    city = models.CharField("Ciudad", max_length=100)
    propietario_cliente = models.ForeignKey(modelos_g_clientes.Cliente, on_delete=models.CASCADE, null=True, blank=True)
    propietario_mensajero = models.ForeignKey(modelos_g_mensajeros.Mensajeros, on_delete=models.CASCADE, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photo', null=True, blank=True)
