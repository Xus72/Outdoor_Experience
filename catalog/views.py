from django.shortcuts import render
from django.views import generic

from .models import Proveedor, Actividad, Guia, Participante

def index(request):
    #Contador de actividades
    num_actividades = Actividad.objects.all().count()
    #Contador de guias
    num_guias = Guia.objects.all().count()

    return render(request, 'index.html', context={'num_actividades':num_actividades, 'num_guias':num_guias},)

class Actividades(generic.ListView):
    model = Actividad
    paginate_by = 1

class Guias(generic.ListView):
    model = Guia
    paginate_by = 10

class ActividadesDetailView(generic.DetailView):
    model = Actividad

class GuiasDetailView(generic.DetailView):
    model = Guia