from django.urls import path
from MVTEstudioGrabacion.views import inicio, musicos, cantantes, empleados, discos, contacto

urlpatterns = [
    path('', inicio),
    path('musicos/', musicos),
    path('cantantes/', cantantes),
    path('empleados/', empleados),
    path('discos/', discos),
    path('contacto/', contacto)
]