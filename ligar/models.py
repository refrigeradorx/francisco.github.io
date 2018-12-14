from django.db import models 
from cliente.models import Cliente
from index.models import Perfil

class Asignar(models.Model):
    tecnico = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    cliente = models.OneToOneField(Cliente,on_delete=models.CASCADE,unique = True)