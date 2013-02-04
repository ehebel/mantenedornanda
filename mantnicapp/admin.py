from django.contrib import admin
from mantenedornanda.mantnicapp.models import nic, nicActividad, nicCampo, nicClase, nicEspecialidad, relacionNandaNic

class NicAdmin(admin.ModelAdmin):
    list_display = ('titulo','tituloabreviado','revisado')
    list_filter = ('revisado')

class NandaNicAdmin(admin.ModelAdmin):
    list_display = ('titulos_nanda','titulos_nic','prioridad_relacion')
    def titulos_nanda(self, obj):
        return '%s'%obj.nanda.titulo
    titulos_nanda.short_description = 'Titulos NANDA'
    def titulos_nic(self, obj):
        return '%s'%obj.nic.titulo
    titulos_nic.short_description = 'Titulos NIC'
    def prioridad_relacion(self, obj):
        return '%s'%obj.prioridad.titulo
    prioridad_relacion.short_description = 'Prioridad'
    list_display_links = ('titulos_nanda','titulos_nic')



admin.site.register(nic,NicAdmin)
admin.site.register(nicActividad)
admin.site.register(nicCampo)
admin.site.register(nicClase)
admin.site.register(nicEspecialidad)
admin.site.register(relacionNandaNic,NandaNicAdmin)


__author__ = 'ehebel'
