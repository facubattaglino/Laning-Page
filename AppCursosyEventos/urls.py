from django.urls import path
from .views import * 

urlpatterns = [
    path('', inicio, name= "inicio"),
    path('cursos/', cursos, name= "cursos"),
    path('crear_curso/', crear_curso, name = "crar_curso"),
    path('profesores/', profesores , name= "profesores"),
    path('alumnos/', alumno , name= "alumnos" )
]