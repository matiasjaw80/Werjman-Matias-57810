from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import Entregable, Estudiante, Curso, Profesor


class CursoFormulario(ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'comision', 'codigo', 'imagen']


class ProfesorFormulario(ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'profesion']


class EntregableFormulario(ModelForm):
    class Meta:
        model = Entregable
        fields = ['nombre', 'fecha_entrega', 'entregado', 'estudiante']


class EstudianteFormulario(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']



#__________________________________________________________________________

class RegistroUsuariosForm(UserCreationForm):      
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserEditForm(UserChangeForm):
    email = forms.EmailField(label="Email de Usuario", required=True)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)   
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']



class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)