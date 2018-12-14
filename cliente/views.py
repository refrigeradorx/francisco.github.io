from .models import Cliente
from django.shortcuts import render,redirect
from .forms import ClienteForm

# Create your views here.

def formulario(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente')
    else:
        form = ClienteForm()
    return render(request,'cliente/cliente.html',{'form': form})