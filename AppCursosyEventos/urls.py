from django.urls import path
from .views import * 

urlpatterns = [
    path('', inicio, name= "inicio"),
    path('cursos/', cursos, name= "cursos"),
    path('eventos/', eventos , name= "eventos")
    
]