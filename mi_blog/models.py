
# Create your models here.
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    apellido = models.CharField(max_length=256)

class Familiares(Persona):
    parentesco = models.CharField(max_length=50)
    

class Amigos(Persona):
    nivel_amistad = models.PositiveIntegerField()

class Viajes(models.Model):
    destino = models.CharField(max_length=100)
    duracion = models.IntegerField()
    fecha_viaje = models.DateField()
    viajeros = models.ManyToManyField(Persona)
