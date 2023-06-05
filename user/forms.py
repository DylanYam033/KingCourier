from user.models import User
from django import forms
# Para crear un form personalizado, debemos crear dentro de nuestra app un archivo form.py y dentro de el ponemos el modelo en el cual se va a basar para realizar el form

class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'num_phone', 'address', 'city', 'propietario_cliente', 'propietario_mensajero', 'profile_photo')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            # Si se está editando un perfil existente, se ocultan los campos específicos
            self.fields.pop('propietario_cliente')
            self.fields.pop('propietario_mensajero')
            self.fields.pop('password1')
            self.fields.pop('password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        password1 = self.cleaned_data.get('password1')
        if password1:
            user.set_password(password1)
        if commit:
            user.save()
        return user




