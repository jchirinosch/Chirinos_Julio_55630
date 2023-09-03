from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

###Forms puntos de menú web / alta de usuario / avatar

class GuitarrasForm(forms.Form):
    marca = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    origen = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)

class BajosForm(forms.Form):
    marca = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    origen = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)

class PercusionForm(forms.Form):
    marca = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    origen = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True) 

class SucursalForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    direccion = forms.CharField(max_length=500, required=True)
    email = forms.EmailField(required=True)
    telefono = forms.IntegerField(required=True)

class RegistroUsuariosForm(UserCreationForm):      
    email = forms.EmailField(label="Email del usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
 
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)   
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)   

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class AvatarFormulario(forms.Form):
        imagen = forms.ImageField(required=True)