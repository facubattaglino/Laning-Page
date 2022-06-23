from django.contrib import admin
from .models import *

class CursoAdmin(admin.ModelAdmin):

    list_display = (
        "cursos",
    )

class ProfresoresAdmin(admin.ModelAdmin):

    list_display = (
        "nombre",
        "apellido",
        )

class AlumnosAdmin(admin.ModelAdmin):

    list_display = (
        "nombre",
        "apellido",
        "edad",
        "nacimiento",
        )

admin.site.register(Cursos, CursoAdmin)
admin.site.register(Profesores, ProfresoresAdmin)
admin.site.register( Alumnos, AlumnosAdmin)