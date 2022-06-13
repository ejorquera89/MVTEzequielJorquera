from django import forms

class MusicoForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    instrumento = forms.CharField(max_length=20)


class CantanteForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    tipodevoz = forms.CharField(max_length=15)


class EmpleadoForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)


class DiscoForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    fechaDeEstreno = forms.DateField()
    Productora = forms.CharField(max_length=20)

