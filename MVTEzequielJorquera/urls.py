from django.contrib import admin
from django.urls import path
from MVTEstudioGrabacion.views import plantilla

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', plantilla),
]
