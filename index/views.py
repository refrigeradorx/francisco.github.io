from django.shortcuts import render,redirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .models import Perfil
from .forms import SignUpForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LoginView, LogoutView 
# Create your views here.

def post_list(request):
    return render(request, 'index/indesssx.html', {})

def Login(request):
    return render(request, 'index/Login.html', {})

class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class SignInView(LoginView):
    template_name = 'index/iniciar_sesion.html'

class BienvenidaView(TemplateView):
    template_name = 'index/indesssx.html'

class SignOutView(LogoutView):
    pass

