from django.urls import path
from .views import * 
from .forms import * 

urlpatterns = [
    path('', inicio, name= "inicio"),
    path('login', login_request , name="login"), #no usar login como nombre de la vista
    
    path('cursos/', cursos, name= "cursos"),
    path('crear_curso/', crear_curso, name = "crear_curso"),
    path('buscar_curso/', buscar_curso, name ="buscar_curso"),
    
    path('profesores/', profesores , name= "profesores"),
    path('crear_profesor/', crear_profesor , name= "crear_profesor"),
    path('buscar_profesor/', buscar_profesor, name = "buscar_profesor"),
    
    path('alumnos/', alumno , name= "alumnos" ),
    path('crear_alumnos/', crear_alumno, name= "crear_alumnos"),
    path('buscar_alumno/', buscar_alumno, name= "buscar_alumno"),
    path('eliminar_alumno/<alumno_id>', eliminar_alumno, name= "eliminar_alumno"),
    path('editar_alumno/<alumno_id>', editar_alumno, name= "editar_alumno"),
    
    # path('alumno/list', AlumnosList.as_view() , name= "alumnos_list" ),
    # path(r'^(?P<pk>\d+)$', AlumnosDetail.as_view(), name= "alumnos_detail" ),
    # path(r'^nuevo$', AlumnoCreate.as_view() , name= "alumnos_create" ),
    # path(r'^editar/(?P<pk>\d+)$', AlumnoUpdate.as_view() , name= "alumnos_update" ),
    # path(r'^eliminar/(?P<pk>\d+)$', AlumnoDelete.as_view() , name= "alumnos_delete" ),
]
#    #<pk> es el parametro que voy a recibir (tipo "id")