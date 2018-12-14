from django.conf.urls import url
from .views import asignar,asignar_lista
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^ligar$',asignar, name='ligar'),
    url(r'^listaligar$', asignar_lista, name='listaligar'),

    
]

