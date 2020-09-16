from django.contrib import admin
from .models import Proveedor, Actividad, Guia, Participante

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipoEntidad','localidad')
    list_filter = ['nombre', 'tipoEntidad', 'localidad']

admin.site.register(Proveedor,ProveedorAdmin)

class ActividadAdmin(admin.ModelAdmin):
    list_display = ('titulo','fechaSalida','fechaRecogida', 'lugar', 'proveedor', 'geometria', 'tipo', 'medio', 'modalidad', 'ambito', 'tematica', 'nivel')
    list_filter = ['titulo','fechaSalida','fechaRecogida', 'lugar', 'proveedor', 'geometria', 'tipo', 'medio', 'modalidad', 'ambito', 'tematica', 'nivel']

admin.site.register(Actividad,ActividadAdmin)

class GuiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos','fechaNacimiento', 'sexo')
    list_filter = ['sexo']

admin.site.register(Guia,GuiaAdmin)

class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellidos', 'fechaNacimiento', 'municipio', 'provincia', 'nacionalidad')
    list_filter = ['municipio', 'provincia', 'nacionalidad']

admin.site.register(Participante,ParticipanteAdmin)
