from re import M
from statistics import mode
from django.db import models

# Create your models here.
class Cursos(models.Model):
    cursos = models.CharField(max_length= 30)
    comision = models.PositiveIntegerField()

class Profesores(models.Model):
    nombre = models.CharField(max_length= 30)
    apellido = models.CharField(max_length= 30)
    
class Alumnos(models.Model):
    nombre = models.CharField(max_length= 30)
    apellido = models.CharField(max_length= 30)
    edad = models.PositiveIntegerField()
    nacimiento = models.DateField()