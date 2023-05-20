from django.forms import ModelForm
from .models import Mensajeros

class MensajeroForm(ModelForm):
    class Meta:
        model = Mensajeros
        fields = ['identificacion', 'nombre', 'direccion', 'ciudad', 'email', 'telefono', 'vehiculo']


         
