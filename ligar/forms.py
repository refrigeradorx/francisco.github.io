from django import forms 
from .models import Asignar

class PostForm(forms.ModelForm):
    class Meta:
        model = Asignar   
        fields = [
            'tecnico','cliente',]
        labels = {
            'tecnico': 'Nombre tecnico',
            'cliente': 'Rut cliente',
        }

class ListaForm(forms.ModelForm):
    class Meta:
        model = Asignar
        fields = ('tecnico','cliente',)
       