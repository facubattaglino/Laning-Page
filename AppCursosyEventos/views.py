from django.shortcuts import render
from .models import *
# Create your views here.
def inicio(request):
    
    return render(request,"CursosyEventosApp/index.html")

def cursos(request):
    cursos = Cursos.objects.all()[:3]
    return render(request,"CursosyEventosApp/cursos.html",{"cursos":cursos})

def eventos(request):
    eventos = Eventos.objects.all()[:3]
    return render(request,"CursosyEventosApp/eventos.html",{"eventos":eventos})