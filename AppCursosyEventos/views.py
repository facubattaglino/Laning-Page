from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.db.models import Q

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.contrib.auth.forms import AuthenticationForm #formulario de autenticacion(va a pedir nombre de usuario y contraseña para iniciar sesion)
from django.contrib.auth import login, logout ,authenticate #importo estos metodos


# Create your views here.
def entrada(request):
    return redirect("inicio")

def inicio(request):
    cursos = Cursos.objects.all().order_by('-id')[:3]
    eventos = Profesores.objects.all().order_by('-id')[:3]
    ctx = {'cursos': cursos, 'profes':eventos,}
    return render(request,"CursosyEventosApp/index.html", ctx)

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password')
            user = authenticate(user=username,password=password1)

            if user is not None: #si el formulario es valido, me logueo y voy a pagina inicio
                login(request,user)
                return redirect("inicio")
            else: #si el formulario NO es valido, me redirecciona a pagina login
                return redirect("login")
        else:
            return redirect("login")
    
    form = AuthenticationForm()
    
    return render(request,"CursosyEventosApp/login.html",{"form":form})



def alumno(request):
    if request.method == "POST":
        alumno = request.POST ["alumnoo"] #alumnoo Viene del name=alumnoo en el template
        if alumno !="":
            alumnos = Alumnos.objects.filter( Q(nombre__icontains=alumno) | Q(apellido__icontains=alumno) | Q(fecha_nacimiento__icontains=alumno) ).values()
            return render(request,"CursosyEventosApp/alumnos.html",{"alumnos":alumnos,"alumnoo":True,"busqueda":alumno})
    alumno = Alumnos.objects.all()
    return render(request,"CursosyEventosApp/alumnos.html",{"alumnos":alumno})

def crear_alumno(request):
    #POST 
    if request.method == "POST":
        
        formulario = NuevoAlumno(request.POST)
        
        if formulario.is_valid():
            
            info_alumno = formulario.cleaned_data
            
            alumno= Alumnos(nombre = info_alumno["nombre"],
                            apellido = info_alumno["apellido"],
                            edad = int(info_alumno["edad"]),
                            fecha_nacimiento = info_alumno["fecha_nacimiento"]) #[nombre] es igual a nombre el forms
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

def eliminar_alumno(request, alumno_id): # siempre eliminar por ID nunca por NOMBRES
    alumno = Alumnos.objects.get(id=alumno_id)
    alumno.delete()
    
    return redirect('alumnos')

def editar_alumno(request, alumno_id):
    
    alumno = Alumnos.objects.get(id=alumno_id)
    
    if request.method == "POST":
        
        formulario = NuevoAlumno(request.POST)
        if formulario.is_valid():
            info_alumno = formulario.cleaned_data
            alumno.nombre = info_alumno["nombre"]
            alumno.apellido = info_alumno["apellido"]
            alumno.edad = info_alumno["edad"]
            alumno.fecha_nacimiento = info_alumno["fecha_nacimiento"]
            alumno.save()
            return redirect('alumnos')
    #get
    formulario_vacio = NuevoAlumno(initial={"nombre":alumno.nombre,
                                "apellido":alumno.apellido,
                                "edad":alumno.edad,
                                "fecha_nacimiento":alumno.fecha_nacimiento})
    return render(request,"CursosyEventosApp/form_alumnos.html",{'form':formulario_vacio})


# class AlumnosList(ListView):
#     model = Alumnos #De aca saca los datos que luego mostramos
#     template_name = "CursosyEventosApp/alumno_list.html"

# class AlumnosDetail(DetailView):
#     model = Alumnos
#     template_name = "CursosyEventosApp/alumno_detail.html"

# class AlumnoCreate(CreateView):
#     model = Alumnos
#     success_url = "/appcye/alumnos/list"
#     fields = ["nombre", "apellido", "edad", "fecha_nacimiento"] #Le paso los campos para CREAR

# class AlumnoUpdate(UpdateView):
#     model = Alumnos
#     success_url = "/appcye/alumnos/list"
#     fields = ["nombre", "apellido", "edad", "fecha_nacimiento"] #Le paso los campos para EDITAR

# class AlumnoDelete(DeleteView):
#     model = Alumnos
#     success_url = "/appcye/alumnos/list" #appcye ES LA URLS del proyecto


def cursos(request):
    cursos = Cursos.objects.all()
    return render(request,"CursosyEventosApp/cursos.html",{"cursos":cursos})

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

def buscar_curso(request):
    if request.method == "POST":
        cursos = request.POST["cursos"]
        if cursos !="":
            curso = Cursos.objects.filter( Q(cursos__icontains=cursos) | Q(comision__icontains=cursos)).values()
            return render(request,"CursosyEventosApp/buscar_curso.html",{"curs":curso,"resultado":True})
        
    return render(request,"CursosyEventosApp/buscar_curso.html",{})

def profesores(request):
    profesores = Profesores.objects.all()
    return render(request,"CursosyEventosApp/profesores.html",{"profes":profesores})

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

def buscar_profesor(request):
    if request.method == "POST":
        profesor = request.POST["profesor"]
        if profesor !="":
            
            profesores = Profesores.objects.filter( Q(nombre__icontains=profesor) | Q(apellido__icontains=profesor)).values()
            return render(request,"CursosyEventosApp/buscar_profesor.html",{"profe":profesores,"profesor":True})
        
    return render(request,"CursosyEventosApp/buscar_profesor.html",{})