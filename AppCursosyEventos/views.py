from inspect import formatargvalues
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.db.models import Q


# Create your views here.
def inicio(request):
    cursos = Cursos.objects.all().order_by('-id')[:3]
    eventos = Profesores.objects.all().order_by('-id')[:3]
    ctx = {'cursos': cursos, 'profes':eventos,}
    return render(request,"CursosyEventosApp/index.html", ctx)

def cursos(request):
    cursos = Cursos.objects.all()
    return render(request,"CursosyEventosApp/cursos.html",{"cursos":cursos})

def profesores(request):
    profesores = Profesores.objects.all()
    return render(request,"CursosyEventosApp/profesores.html",{"profes":profesores})

def alumno(request):
    alumno = Alumnos.objects.all()
    return render(request,"CursosyEventosApp/alumnos.html",{"alumnos":alumno})

def crear_curso(request):
    #POST 
    if request.method == "POST":
        
        formulario = NuevoCurso(request.POST)
        
        if formulario.is_valid():
            
            info_curso = formulario.cleaned_data
            
            curso = Cursos(cursos = info_curso["nombre"], comision = int(info_curso["comision"])) #[nombre] es igual a nombre el forms
            
            curso.save()
            
            return redirect("cursos") #render(request,"CursosyEventosApp/form_curso.html")
        
        else:
            redirect("crear_curso")
    else:
        formulario_vacio = NuevoCurso()
    #GET
        return render(request,"CursosyEventosApp/form_curso.html",{'form':formulario_vacio})

def crear_profesor(request):
    #POST 
    if request.method == "POST":
        
        formulario = NuevoPorfesor(request.POST)
        
        if formulario.is_valid():
            
            info_profesor = formulario.cleaned_data
            
            profesor= Profesores(nombre = info_profesor["nombre"], apellido = info_profesor["apellido"]) #[nombre] es igual a nombre el forms
            
            profesor.save()
            
            return redirect("profesores") #render(request,"CursosyEventosApp/form_curso.html")
        
        else:
            redirect("crear_profesor")
    else:
        formulario_vacio = NuevoPorfesor()
    #GET
        return render(request,"CursosyEventosApp/form_profesores.html",{'form':formulario_vacio})    

def crear_alumno(request):
    #POST 
    if request.method == "POST":
        
        formulario = NuevoAlumno(request.POST)
        
        if formulario.is_valid():
            
            info_alumno = formulario.cleaned_data
            
            alumno= Alumnos(nombre = info_alumno["nombre"],
                            apellido = info_alumno["apellido"],
                            edad = int(info_alumno["edad"]),
                            nacimiento = info_alumno["fecha_nacimiento"]) #[nombre] es igual a nombre el forms
            alumno.save()
            
            return redirect("alumnos") #render(request,"CursosyEventosApp/form_curso.html")
        
        else:
            redirect("crear_alumnos")
    else:
        formulario_vacio = NuevoAlumno()
    #GET
        return render(request,"CursosyEventosApp/form_alumnos.html",{'form':formulario_vacio})

def buscar_alumno(request):
    if request.method == "POST":
        alumno = request.POST ["alumno"]
        if alumno !="":
            alumnos = Alumnos.objects.filter( Q(nombre__icontains=alumno) | Q(apellido__icontains=alumno) | Q(nacimiento__icontains=alumno) ).values()
            return render(request,"CursosyEventosApp/buscar_alumno.html",{"alumnosss":alumnos,"alumno":True})
        
    return render(request,"CursosyEventosApp/buscar_alumno.html",{})

def buscar_curso(request):
    if request.method == "POST":
        cursos = request.POST["cursos"]
        if cursos !="":
            curso = Cursos.objects.filter( Q(cursos__icontains=cursos) | Q(comision__icontains=cursos)).values()
            return render(request,"CursosyEventosApp/buscar_curso.html",{"curs":curso,"resultado":True})
        
    return render(request,"CursosyEventosApp/buscar_curso.html",{})

def buscar_profesor(request):
    if request.method == "POST":
        profesor = request.POST["profesor"]
        if profesor !="":
            
            profesores = Profesores.objects.filter( Q(nombre__icontains=profesor) | Q(apellido__icontains=profesor)).values()
            return render(request,"CursosyEventosApp/buscar_profesor.html",{"profe":profesores,"profesor":True})
        
    return render(request,"CursosyEventosApp/buscar_profesor.html",{})