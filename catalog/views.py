from django.shortcuts import render

from .models import Proveedor, Actividad, Guia, Participante

def index(request):
    #Contador de actividades
    num_actividades = Actividad.objects.all().count()
    #Contador de guias
    num_guias = Guia.objects.all().count()

    return render(request, 'index.html', context={'num_actividades':num_actividades, 'num_guias':num_guias},)