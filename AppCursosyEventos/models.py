from statistics import mode
from django.db import models

# Create your models here.
class Cursos(models.Model):
    cursos = models.CharField(max_length= 30)

class Eventos(models.Model):
    eventos = models.CharField(max_length= 30)
    fecha = models.DateField()