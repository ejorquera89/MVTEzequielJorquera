from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.

def inicio(self):
    plantilla = loader.get_template('MVTEstudioGrabacion/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def musicos(request):
    return render (request, 'MVTEstudioGrabacion/musicos.html')

def cantantes(request):
    documento = f" Cantantes "
    return render (request, 'MVTEstudioGrabacion/cantantes.html')

def empleados(request):
    return render (request, 'MVTEstudioGrabacion/empleados.html')

def discos(request):
    return render (request, 'MVTEstudioGrabacion/discos.html')

def contacto(request):
    return render (request, 'MVTEstudioGrabacion/contacto.html')



