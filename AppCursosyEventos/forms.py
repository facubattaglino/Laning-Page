from tabnanny import verbose
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NuevoCurso(forms.Form):
    nombre = forms.CharField(max_length=30,label="Nombre Curso")  #nombre es igual a nombre el views [nombre]
    comision = forms.IntegerField(min_value=0, label="Numero de Comision")

class NuevoPorfesor(forms.Form):
    nombre = forms.CharField(max_length=30,label="Nombre")  #nombre es igual a nombre el views [nombre]
    apellido = forms.CharField(max_length=30, label="Apellido")

class NuevoAlumno(forms.Form):
    nombre = forms.CharField(max_length=30,label="Nombre")  #nombre es igual a nombre el views [nombre]
    apellido = forms.CharField(max_length=30, label="Apellido")
    edad = forms.IntegerField(min_value=0, label= "Edad")
    fecha_nacimiento = forms.DateField()
#label= "Nombre Curso" es como me lo muestra al campo en la pag... en base de datos queda guardado como nombre
class UserRegisterForm(UserCreationForm):

    
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        help_texts = {k:"" for k in fields}

#Este formulario se utiliza en el template de "editar_perfil"
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)
    
    
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        # help_texts = {k:"" for k in fields}