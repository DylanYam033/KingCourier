from django.forms import ModelForm
from django import forms
from .models import Cliente, Sucursale
# Para crear un form personalizado, debemos crear dentro de nuestra app un archivo form.py y dentro de el ponemos el modelo en el cual se va a basar para realizar el form

class CreateCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = ['identificacion','nombre','direccion', 'ciudad', 'email', 'telefono', 'mensajeros']


class SucursaleForm(ModelForm):
    class Meta:
        model = Sucursale
        fields = ['nombre', 'direccion', 'telefono', 'ciudad']