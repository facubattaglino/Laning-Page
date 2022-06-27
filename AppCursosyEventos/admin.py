from django.contrib import admin
from .models import *

class CursoAdmin(admin.ModelAdmin):

    list_display = (
        "cursos",
        "comision",
    )
    search_fields = ("cursos","comision")

class ProfresoresAdmin(admin.ModelAdmin):

    list_display = (
        "nombre",
        "apellido",
        )
    search_fields = ("nombre","apellido")
class AlumnosAdmin(admin.ModelAdmin):

    list_display = (
        "nombre",
        "apellido",
        "edad",
        "nacimiento",
        )
    search_fields = ("nombre","apellido","edad","nacimiento")

admin.site.register(Cursos, CursoAdmin)
admin.site.register(Profesores, ProfresoresAdmin)
admin.site.register( Alumnos, AlumnosAdmin)