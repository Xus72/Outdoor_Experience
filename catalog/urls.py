from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^actividades', views.Actividades.as_view(), name='actividades'),
    url(r'^actividad/(?P<pk>\d+)$', views.ActividadesDetailView.as_view(), name='actividades-detalles'),
    url(r'^guias', views.Guias.as_view(), name='guias'),
    url(r'^guias/(?P<pk>\d+)$', views.GuiasDetailView.as_view(), name='guias-detalles')
]