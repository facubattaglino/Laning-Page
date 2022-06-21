from django.contrib import admin
from .models import *

class CursoAdmin(admin.ModelAdmin):

    list_display = (
        "cursos",
    )

class EventosAdmin(admin.ModelAdmin):

    list_display = (
        "eventos",
        "fecha",
        )

admin.site.register(Cursos, CursoAdmin)
admin.site.register(Eventos, EventosAdmin)