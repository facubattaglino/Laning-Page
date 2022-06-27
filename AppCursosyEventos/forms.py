from tabnanny import verbose
from django import forms



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