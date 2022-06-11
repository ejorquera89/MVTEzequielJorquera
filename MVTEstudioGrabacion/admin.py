from django.contrib import admin
from .models import Musico, Cantante, Empleado, Disco

# Register your models here.
admin.site.register(Musico)
admin.site.register(Cantante)
admin.site.register(Empleado)
admin.site.register(Disco)

