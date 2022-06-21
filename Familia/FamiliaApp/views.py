from datetime import datetime
from unittest import loader
from xml.dom.minidom import Document
from django import http
from django.shortcuts import render

from FamiliaApp.models import familiar

from django.http import HttpResponse
from django.template import Context, Template, loader
import datetime

# Create your views here.


def crearFamiliar(request):


    nombre = "tobias"

    edad = 22

    nacimiento = datetime.datetime(2002, 4, 13)

    familiar1 = familiar(nombre=nombre, edad=edad, nacimiento=nacimiento)

    familiar1.save()

    diccionario = {"nombre": nombre, "edad": edad, "nacimiento": nacimiento}

    plantilla = loader.get_template('index.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)


    


