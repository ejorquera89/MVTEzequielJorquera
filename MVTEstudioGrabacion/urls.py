from django.urls import path
from MVTEstudioGrabacion.views import inicio, leerMusico, musicos, cantantes, empleados, discos, contacto, musicosForm, cantanteForm, empleadoForm, discoForm, busquedaMusico, buscar, leerMusico

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('musicos/', leerMusico, name = 'musicos'),
    path('cantantes/', cantantes, name = 'cantantes'),
    path('empleados/', empleados, name = 'empleados'),
    path('discos/', discos, name = 'discos'),
    path('contacto/', contacto, name = 'contacto'),
    path('musicosForm/', musicosForm, name = 'musicosForm'),
    path('cantanteForm/', cantanteForm, name = 'cantantesForm'),
    path('empleadoForm/', empleadoForm, name = 'empleadosForm'),
    path('discoForm/', discoForm, name = 'discoForm'),
    path('busquedaMusico/', busquedaMusico, name = 'busquedaMusico'),
    path('buscar/', buscar, name = 'buscar'),
]