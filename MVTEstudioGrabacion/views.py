from multiprocessing import context
from pickle import GET
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from MVTEstudioGrabacion.models import Musico, Cantante, Empleado, Disco
from django.template import loader
from MVTEstudioGrabacion.forms import MusicoForm
from MVTEstudioGrabacion.forms import CantanteForm
from MVTEstudioGrabacion.forms import EmpleadoForm
from MVTEstudioGrabacion.forms import DiscoForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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

def leerCantante(request):
    cantantes = Cantante.objects.all()
    contexto = {'cantantes': cantantes}
    return render (request, 'MVTEstudioGrabacion/cantantes.html', contexto)

def leerEmpleado(request):
    empleados = Empleado.objects.all()
    contexto = {'empleados': empleados}
    return render (request, 'MVTEstudioGrabacion/empleados.html', contexto)

def leerDisco(request):
    discos = Disco.objects.all()
    contexto = {'discos': discos}
    return render (request, 'MVTEstudioGrabacion/discos.html', contexto)

def about(request):
    return render (request, 'MVTEstudioGrabacion/about.html')

#Views de eliminación

def eliminarMusico(request, nombre):
    musico= Musico.objects.get(nombre=nombre)
    musico.delete()

    musico=Musico.objects.all()
    contexto= {'musicos':musico}
    return render (request, 'MVTEstudioGrabacion/musicos.html', contexto)

def eliminarCantante(request, nombre):
    cantante= Cantante.objects.get(nombre=nombre)
    cantante.delete()

    cantante=Cantante.objects.all()
    contexto= {'cantantes':cantante}
    return render (request, 'MVTEstudioGrabacion/cantantes.html', contexto)

def eliminarEmpleado(request, nombre):
    empleados= Empleado.objects.get(nombre=nombre)
    empleados.delete()

    empleados=Empleado.objects.all()
    contexto= {'empleados':empleados}
    return render (request, 'MVTEstudioGrabacion/empleados.html', contexto)

def eliminarDisco(request, nombre):
    discos = Disco.objects.get(nombre=nombre)
    discos.delete()

    discos=Disco.objects.all()
    contexto= {'discos':discos}
    return render (request, 'MVTEstudioGrabacion/discos.html', contexto)

#Views de Edición

def editarMusico(request, nombre):
    musico=Musico.objects.get(nombre=nombre)
    if request.method == 'POST':
        miFormulario = MusicoForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            musico.nombre = informacion['nombre']
            musico.apellido = informacion['apellido']
            musico.email = informacion['email']
            musico.instrumento = informacion['instrumento']
            musico.save()

            musicos = Musico.objects.all()
            contexto = {'musicos':musicos}
            return render (request, 'MVTEstudioGrabacion/musicos.html', contexto)
    else:
        miFormulario = MusicoForm(initial= {'nombre':musico.nombre, 'apellido': musico.apellido, 'email':musico.email, 'instrumento':musico.instrumento})
        contexto = {'miFormulario': miFormulario, 'nombre':nombre}
        return render(request, 'MVTEstudioGrabacion/editarMusico.html', contexto)

def editarCantante(request, nombre):
    cantante=Cantante.objects.get(nombre=nombre)
    if request.method == 'POST':
        miFormulario = CantanteForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cantante.nombre = informacion['nombre']
            cantante.apellido = informacion['apellido']
            cantante.email = informacion['email']
            cantante.tipodevoz = informacion['tipodevoz']
            cantante.save()

            cantantes = Cantante.objects.all()
            contexto = {'cantantes':cantantes}
            return render (request, 'MVTEstudioGrabacion/cantantes.html', contexto)
    else:
        miFormulario = CantanteForm(initial= {'nombre':cantante.nombre, 'apellido': cantante.apellido, 'email':cantante.email, 'tipodevoz':cantante.tipodevoz})
        contexto = {'miFormulario': miFormulario, 'nombre':nombre}
        return render(request, 'MVTEstudioGrabacion/editarCantante.html', contexto)

def editarEmpleado(request, nombre):
    empleado=Empleado.objects.get(nombre=nombre)
    if request.method == 'POST':
        miFormulario = EmpleadoForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            empleado.nombre = informacion['nombre']
            empleado.apellido = informacion['apellido']
            empleado.email = informacion['email']
            empleado.profesion = informacion['profesion']
            empleado.save()

            empleados = Empleado.objects.all()
            contexto = {'empleados':empleados}
            return render (request, 'MVTEstudioGrabacion/empleados.html', contexto)
    else:
        miFormulario = EmpleadoForm(initial= {'nombre':empleado.nombre, 'apellido': empleado.apellido, 'email':empleado.email, 'profesion':empleado.tipodevoz})
        contexto = {'miFormulario': miFormulario, 'nombre':nombre}
        return render(request, 'MVTEstudioGrabacion/editarEmpleado.html', contexto)


def editarDisco(request, nombre):
    disco=Disco.objects.get(nombre=nombre)
    if request.method == 'POST':
        miFormulario = DiscoForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            disco.nombre = informacion['nombre']
            disco.fechaDeEstreno = informacion['fechaDeEstreno']
            disco.Productora = informacion['productora']
            disco.save()

            discos = Disco.objects.all()
            contexto = {'discos':discos}
            return render (request, 'MVTEstudioGrabacion/discos.html', contexto)
    else:
        miFormulario = DiscoForm(initial= {'nombre':disco.nombre, 'fechaDeEstreno': disco.fechaDeEstreno, 'Productora':disco.Productora})
        contexto = {'miFormulario': miFormulario, 'nombre':nombre}
        return render(request, 'MVTEstudioGrabacion/editarDisco.html', contexto)

#Clases basadas en Vistas

#LISTVIEW
class MusicoList(ListView):
    modelo = Musico
    template_name = 'MVTEstudioGrbacion/musicos.html'

#DETAILVIEW

class MusicoDetail(DetailView):
    modelo = Musico
    template_name = 'MVTEstudioGrabacion/musicoDetalle.html'

#CREATEVIEW

class MusicoCreate(CreateView):
    modelo = Musico
    success_url = reverse_lazy('musicos')
    fields = ['nombre', 'apellido', 'email', 'instrumento']

#EDITVIEW

class MusicoEdit(UpdateView):
    modelo = Musico
    success_url = reverse_lazy('musicos')
    fields = ['nombre', 'apellido', 'email', 'instrumento']

#DELETEVIEW

class MusicoEliminar(DeleteView):
    modelo = Musico
    success_url = reverse_lazy('musicos')