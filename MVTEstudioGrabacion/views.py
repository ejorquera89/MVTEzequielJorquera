from django import http
from django.shortcuts import render
from django.template import loader
# Create your views here.

def plantilla(self):
    plantilla = loader.get_template('plantilla.html')
    documento = plantilla.render()
    return http.HttpResponse(documento)
