from django.urls import path
from MVTEstudioGrabacion.views import MusicoCreate, MusicoDetail, MusicoEdit, MusicoEliminar, MusicoList, editarCantante, editarDisco, editarEmpleado, editarMusico, eliminarCantante, eliminarDisco, eliminarEmpleado, eliminarMusico, inicio, musicos, leerCantante, leerEmpleado, leerDisco, contacto, musicosForm, cantanteForm, empleadoForm, discoForm, busquedaMusico, buscar, leerMusico, about

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('musicos/', leerMusico, name = 'musicos'),
    path('cantantes/', leerCantante, name = 'cantantes'),
    path('empleados/', leerEmpleado, name = 'empleados'),
    path('discos/', leerDisco, name = 'discos'),
    path('contacto/', contacto, name = 'contacto'),
    path('musicosForm/', musicosForm, name = 'musicosForm'),
    path('cantanteForm/', cantanteForm, name = 'cantantesForm'),
    path('empleadoForm/', empleadoForm, name = 'empleadosForm'),
    path('discoForm/', discoForm, name = 'discoForm'),
    path('busquedaMusico/', busquedaMusico, name = 'busquedaMusico'),
    path('buscar/', buscar, name = 'buscar'),
    path('about/', about, name='about'),
    path('eliminarMusico/<nombre>', eliminarMusico, name='eliminarMusico'),
    path('eliminarCantante/<nombre>', eliminarCantante, name='eliminarCantante'),
    path('eliminarEmpleado/<nombre>', eliminarEmpleado, name='eliminarEmpleado'),
    path('eliminarDisco/<nombre>', eliminarDisco, name='eliminarDisco'),
    path('editarMusico/<nombre>', editarMusico, name='editarMusico'),
    path('editarCantante/<nombre>', editarCantante, name='editarCantante'),
    path('editarDisco/<nombre>', editarDisco, name='editarDisco'),
    path('editarEmpleado/<nombre>', editarEmpleado, name='editarEmpleado'),

    path('musico/list/', MusicoList.as_view(), name='musico_list'),
    path('musico/<pk>/', MusicoDetail.as_view(), name='musico_detalle'),
    path('musico/nuevo/', MusicoCreate.as_view(), name='musico_crear'),
    path('musico/edicion/<pk>', MusicoEdit.as_view(), name='musico_editar'),
    path('musico/borrar/<pk>', MusicoEliminar.as_view(), name='musico_eliminar'),
]