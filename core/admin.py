
from django.contrib import admin
from django.contrib.admin import models
from .models import Atencion, Usuario, Reserva, Box
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class UsuarioResource(resources.ModelResource):
    class Meta:
        model = Usuario

class UsuarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['rut','email']
    list_display = ['id','nombre','apellido','rut','email','usuario_administrador','especialidad']
    resources_class = UsuarioResource

class ReservaResource(resources.ModelResource):
    class Meta:
        model = Reserva

class ReservaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['dia_reservado','usuario_id']
    list_display = ['dia_reservado','usuario_id']
    resource_class = ReservaResource

class BoxResource(resources.ModelResource):
    class Meta:
        model = Box

class BoxAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id','estado','especialidad']
    list_display = ['id','estado','especialidad']
    resource_class = BoxResource


class AtencionResource(resources.ModelResource):
    class Meta:
        model = Atencion

class AtencionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id','reserva_id','box']
    list_display = ['id','reserva_id','especialista','box']
    resource_class = AtencionResource

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Reserva,ReservaAdmin)
admin.site.register(Box,BoxAdmin)
admin.site.register(Atencion, AtencionAdmin)