from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver

class Cliente(models.Model):
    rut = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=140)
    direccion = models.CharField(max_length=140)
    ciudad = models.CharField(max_length=140)
    comuna = models.CharField(max_length=140)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=140)
