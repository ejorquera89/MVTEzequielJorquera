from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from MVTEstudioGrabacion.models import Musico, Cantante, Empleado, Disco
from django.template import loader
from MVTEstudioGrabacion.forms import MusicoForm
from MVTEstudioGrabacion.forms import CantanteForm
from MVTEstudioGrabacion.forms import EmpleadoForm
from MVTEstudioGrabacion.forms import DiscoForm

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

#Views de Formularios

def musicosForm(request):
    if request.method == 'POST':
        miFormulario = MusicoForm(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
        nombre = data ['nombre']
        apellido = data ['apellido']
        email = data ['email']
        instrumento = data['instrumento']
        musico = Musico(nombre = nombre, apellido = apellido, email = email, instrumento = instrumento)
        musico.save()
        return render (request, 'MVTEstudioGrabacion/inicio.html')
    else:   
        miFormulario = MusicoForm()
    return render (request, 'MVTEstudioGrabacion/musicosForm.html', {'miFormulario': miFormulario})

def cantanteForm(request):
    if request.method == 'POST':
        miFormulario = CantanteForm(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
        nombre = data ['nombre']
        apellido = data ['apellido']
        email = data ['email']
        tipodevoz = data ['tipodevoz']
        cantante = Cantante(nombre = nombre, apellido = apellido, email = email, tipodevoz = tipodevoz)
        cantante.save()
        return render (request, 'MVTEstudioGrabacion/inicio.html')
    else:
        miFormulario = CantanteForm()
    return render (request, 'MVTEstudioGrabacion/cantantesForm.html', {'miFormulario': miFormulario})

def empleadoForm(request):
    if request.method == 'POST':
        miFormulario = EmpleadoForm(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
        nombre = data ['nombre']
        apellido = data ['apellido']
        email = data ['email']
        profesion = data['profesion']
        empleado = Empleado(nombre = nombre, apellido = apellido, email = email, profesion = profesion)
        empleado.save()
        return render (request, 'MVTEstudioGrabacion/inicio.html')
    else:
        miFormulario = EmpleadoForm()
    return render (request, 'MVTEstudioGrabacion/empleadosForm.html', {'miFormulario': miFormulario})

def discoForm(request):
    if request.method == 'POST':
        miFormulario = DiscoForm(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
        nombre = data ['nombre']
        fechaDeEstreno = data ['fechaDeEstreno']
        Productora = data['Productora']
        disco = Disco(nombre = nombre, fechaDeEstreno = fechaDeEstreno, Productora = Productora)     
        disco.save()
        return render (request, 'MVTEstudioGrabacion/inicio.html')
    else:
        miFormulario = DiscoForm()
    return render (request, 'MVTEstudioGrabacion/discoForm.html', {'miFormulario': miFormulario})

# Views de Búsqueda    

def busquedaMusico(request):
    return render (request, 'MVTEstudioGrabacion/busquedaMusico.html')

def buscar(request):
    #respuesta = f"Estoy buscando al músico {request.GET['apellido']}"
    #return HttpResponse(respuesta)
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        musico = Musico.objects.filter(nombre = nombre)
        return render(request, 'MVTEstudioGrabacion/resultadosBusqueda.html', {'musico': musico, 'nombre': nombre})
    else:
        respuesta = "No ha ingresado datos"
        return HttpResponse(respuesta)

def leerMusico(request):
    musicos = Musico.objects.all()
    contexto = {'musicos': musicos}
    return render (request, 'MVTEstudioGrabacion/musicos.html', contexto)
