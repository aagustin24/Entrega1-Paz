from django.db import models

# Create your models here.

class Cliente(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)

class Auto(models.Model):
    
    patente=models.CharField(max_length=40)
    modelo=models.CharField(max_length=40)

class Servicio(models.Model):

    lavado=models.CharField(max_length=40)
    pulido=models.CharField(max_length=40)