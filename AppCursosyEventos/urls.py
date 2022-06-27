from django.urls import path
from .views import * 
from .forms import * 

urlpatterns = [
    path('', inicio, name= "inicio"),
    path('cursos/', cursos, name= "cursos"),
    path('crear_curso/', crear_curso, name = "crear_curso"),
    path('buscar_curso/', buscar_curso, name ="buscar_curso"),
    path('profesores/', profesores , name= "profesores"),
    path('crear_profesor/', crear_profesor , name= "crear_profesor"),
    path('buscar_profesor/', buscar_profesor, name = "buscar_profesor"),
    path('alumnos/', alumno , name= "alumnos" ),
    path('crear_alumnos/', crear_alumno, name= "crear_alumnos"),
    path('buscar_alumno/', buscar_alumno, name= "buscar_alumno"),
]