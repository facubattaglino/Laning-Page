from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def inicio(request):
    cursos = Cursos.objects.all()[:3]
    eventos = Profesores.objects.all()[:3]
    ctx = {'cursos': cursos, 'profes':eventos,}
    return render(request,"CursosyEventosApp/index.html", ctx)

def cursos(request):
    cursos = Cursos.objects.all()[:3]
    return render(request,"CursosyEventosApp/cursos.html",{"cursos":cursos})

def profesores(request):
    profesores = Profesores.objects.all()[:3]
    return render(request,"CursosyEventosApp/profesores.html",{"profes":profesores})

def alumno(request):
    alumno = Alumnos.objects.all()
    return render(request,"CursosyEventosApp/alumnos.html",{"alumnos":alumno})

def crear_curso(request):
    #POST 
    if request.method == "POST":
        
        info_formulario = request.POST
        
        curso = Cursos(nombre = info_formulario["curso"], comision = int(info_formulario["comision"]))
        
        curso.save()
        
        return redirect("inicio") #render(request,"CursosyEventosApp/form_curso.html")
    
    else:
    #GET
        return render(request,"CursosyEventosApp/form_curso.html")
    # post
    # if request.method == "POST":
    #     info_formulario = request.POST
    #     curso = Cursos(nombre=info_formulario["nombre"], comision=int(info_formulario["comision"]))
    #     curso.save()
    #     return redirect("inicio")
    # else: # get y otros
    #     return render(request,"ProyectoCoderApp/formulario_curso.html")