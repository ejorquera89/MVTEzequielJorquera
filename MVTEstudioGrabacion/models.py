from django.db import models

# Create your models here.
class Musico(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    instrumento = models.CharField(max_length=20)

    #def __str__(self) -> str :
        #return self.nombre + " " + str(self.camada)

class Cantante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    tipodevoz = models.CharField(max_length=15)

    #def __str__(self) -> str:
        #return self.nombre + " " + str(self.apellido)   

class Empleado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    #def __str__(self) -> str:
        #return self.nombre + " " + str(self.apellido)

class Disco(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEstreno = models.DateField()
    Productora = models.CharField(max_length=20)