from pydoc import render_doc
import re
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.views.generic import TemplateView
from typing import Any, Dict
from Turnos.forms import *
from Turnos.models import *

# Create your views here.

def inicio(request):
    return render(request, "Turnos/inicio.html")

def clientes(request):

    if request.method == "POST":
            
            miFormulario = ClientesFormulario(request.POST)
            
            print(miFormulario)

            if miFormulario.is_valid:

                informacion = miFormulario.cleaned_data

                clientes = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'] )

                clientes.save()

                return render(request, "Turnos/inicio.html")

    else:

        miFormulario=ClientesFormulario()

    return render(request, "Turnos/clientes.html", {"miFormulario":miFormulario}) 

def auto(request):
    
    if request.method == "POST":
            
            miFormulario = AutoFormulario(request.POST)
            
            print(miFormulario)

            if miFormulario.is_valid:

                informacion = miFormulario.cleaned_data

                auto = Auto(patente=informacion['patente'], modelo=informacion['modelo'] )

                auto.save()

                return render(request, "Turnos/inicio.html")

    else:

        miFormulario=AutoFormulario()

    return render(request, "Turnos/auto.html", {"miFormulario":miFormulario})

def servicio(request):
    
    if request.method == "POST":
            
            miFormulario = ServicioFormulario(request.POST)
            
            print(miFormulario)

            if miFormulario.is_valid:

                informacion = miFormulario.cleaned_data

                servicio = Servicio(lavado=informacion['lavado'], pulido=informacion['pulido'])

                servicio.save()

                return render(request, "Turnos/inicio.html")

    else:

        miFormulario=ServicioFormulario()

    return render(request, "Turnos/servicio.html", {"miFormulario":miFormulario})


def busquedaAuto(request):
    
    return render(request, "Turnos/busquedaAuto.html")

def buscar(request):
    
    if request.GET["modelo"]:
        modelo = request.GET["modelo"]
        auto = Auto.objects.filter(modelo__icontains=modelo)
        return render(request, "D:/Proyecto Coder/Proyecto1/Entrega1-Paz/CarWashEspumita/Turnos/templates/Turnos/resultadoPorBusqueda.html", {"auto":auto, "modelo":modelo})
    
    

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)


