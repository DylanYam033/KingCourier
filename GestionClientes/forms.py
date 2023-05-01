from django.forms import ModelForm
from django import forms
from .models import Cliente, Sucursale
# Para crear un form personalizado, debemos crear dentro de nuestra app un archivo form.py y dentro de el ponemos el modelo en el cual se va a basar para realizar el form

class CreateCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = ['identificacion','nombre','direccion', 'ciudad', 'email', 'telefono']


class SucursaleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(SucursaleForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['cliente'].initial = user.propietario_cliente
    
    class Meta:
        model = Sucursale
        fields = ['nombre', 'direccion', 'telefono', 'ciudad', 'cliente']