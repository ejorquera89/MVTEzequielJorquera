from django.http import HttpResponse
from django.shortcuts import render
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

def musicosForm(request):
    if request.method == 'POST':
        miFormulario = MusicoForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion ['nombre']
        apellido = informacion ['apellido']
        instrumento = informacion['instrumento']
        musico = musico(nombre = nombre, apellido = apellido, instrumento = instrumento)
        musico.save()
        return render (request, 'MVTEstudioGrabacion/inicio.html')
    else:
        miFormulario = MusicoForm()
    return render (request, 'MVTEstudioGrabacion/musicosForm.html', {'miFormulario': miFormulario})

def cantanteForm(request):
    if request.method == 'POST':
        miFormulario = CantanteForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion ['nombre']
        apellido = informacion ['apellido']
        tipodevoz = informacion['tipodevoz']
        cantante = cantante(nombre = nombre, apellido = apellido, tipodevoz = tipodevoz)
        cantante.save()
        return render (request, 'MVTEstudioGrabacion/inicio.html')
    else:
        miFormulario = CantanteForm()
    return render (request, 'MVTEstudioGrabacion/cantantesForm.html', {'miFormulario': miFormulario})

def empleadoForm(request):
    if request.method == 'POST':
        miFormulario = EmpleadoForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion ['nombre']
        apellido = informacion ['apellido']
        profesion = informacion['profesion']
        empleado = empleado(nombre = nombre, apellido = apellido, profesion = profesion)
        empleado.save()
        return render (request, 'MVTEstudioGrabacion/inicio.html')
    else:
        miFormulario = EmpleadoForm()
    return render (request, 'MVTEstudioGrabacion/empleadosForm.html', {'miFormulario': miFormulario})

def discoForm(request):
    if request.method == 'POST':
        miFormulario = DiscoForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion ['nombre']
        fechaDeEstreno = informacion ['fechaDeEstreno']
        productora = informacion['productora']
        disco = disco(nombre = nombre, fechaDeEstreno = fechaDeEstreno, productora = productora)     
        disco.save()
        return render (request, 'MVTEstudioGrabacion/inicio.html')
    else:
        miFormulario = DiscoForm()
    return render (request, 'MVTEstudioGrabacion/discosForm.html', {'miFormulario': miFormulario})