from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^actividades', views.Actividades.as_view(), name='actividades'),
    url(r'^actividad/(?P<pk>\d+)$', views.ActividadesDetailView.as_view(), name='actividades-detalles'),
    url(r'^guias', views.Guias.as_view(), name='guias'),
    url(r'^guia/(?P<pk>\d+)$', views.GuiasDetailView.as_view(), name='guias-detalles'),
    url(r'^actividad/create/$', views.ActividadCreate.as_view(), name='actividad_crear'),
    url(r'^actividad/(?P<pk>\d+)/update/$', views.ActividadUpdate.as_view(), name='actividad_editar'),
    url(r'^actividad/(?P<pk>\d+)/delete/$', views.ActividadDelete.as_view(), name='actividad_eliminar'),
    url(r'^guia/(?P<pk>\d+)/update/$', views.GuiaUpdate.as_view(), name='guia_editar'),
    url(r'^participante/create/$', views.ParticipanteCreate.as_view(), name='participante_crear'),
    url(r'^participante/(?P<pk>\d+)/update/$', views.ParticipanteUpdate.as_view(), name='participante_editar'),
]