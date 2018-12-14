from .models import Asignar
from django.shortcuts import render,redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required  
def asignar(request):
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')
    context =  {
        'form': form,
    }
    return render(request,'ligar/ligar.html',context)


def asignar_lista(request):
    asigna = Asignar.objects.all()
    contexto = {'listas':asigna}
    return render(request, "ligar/listaligar.html", contexto)
    
    