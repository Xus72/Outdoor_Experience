from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Proveedor, Actividad, Guia, Participante

def index(request):
    #Contador de actividades
    num_actividades = Actividad.objects.all().count()
    #Contador de guias
    num_guias = Guia.objects.all().count()

    return render(request, 'index.html', context={'num_actividades':num_actividades, 'num_guias':num_guias},)

class Actividades(generic.ListView):
    model = Actividad
    paginate_by = 10

class Guias(generic.ListView):
    model = Guia
    paginate_by = 10

class ActividadesDetailView(generic.DetailView):
    model = Actividad

class GuiasDetailView(generic.DetailView):
    model = Guia

class ActividadCreate(CreateView):
    model = Actividad
    fields = '__all__'

class ActividadUpdate(UpdateView):
    model = Actividad
    fields = '__all__'

class ActividadDelete(DeleteView):
    model = Actividad
    success_url = reverse_lazy('actividades')

class GuiaUpdate(UpdateView):
    model = Guia
    fields = ['telefono', 'correo', 'password']


class ParticipanteCreate(CreateView):
    model = Participante
    fields = '__all__'

class ParticipanteUpdate(UpdateView):
    model = Participante
    fields = ['municipio', 'provincia', 'codPostal', 'telefono', 'correo', 'password']
