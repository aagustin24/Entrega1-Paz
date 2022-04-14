from django import forms

class ClientesFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()

class AutoFormulario(forms.Form):
    patente=forms.CharField()
    modelo=forms.CharField()

class ServicioFormulario(forms.Form):
    lavado=forms.CharField()
    pulido=forms.CharField()
    