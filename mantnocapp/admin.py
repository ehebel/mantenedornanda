from django.contrib import admin
from mantenedornanda.mantnocapp.models import prioridad, noc, nocClase, nocDominio, nocEscala, nocEspecialidad, nocIndicador, relacionNandaNoc, relacionNicNoc
from mantenedornanda.mantnicapp.models import nic

class NandaNocAdmin(admin.ModelAdmin):
    list_display = ('titulos_nanda','titulos_noc','prioridad_relacion')
    def titulos_nanda(self, obj):
        return '%s'%obj.nanda.titulo
    titulos_nanda.short_description = 'Titulos NANDA'
    def titulos_noc(self, obj):
        return '%s'%obj.noc.titulo
    titulos_noc.short_description = 'Titulos NOC'
    def prioridad_relacion(self, obj):
        return '%s'%obj.prioridad.titulo
    prioridad_relacion.short_description = 'Prioridad'
    list_display_links = ('titulos_nanda','titulos_noc')
    #list_filter = ('prioridad_relacion',)

class NicNocAdmin(admin.ModelAdmin):
    list_display = ('titulos_nic', 'titulos_noc','prioridad_relacion')
    def titulos_nic (self, obj):
        return '%s'%obj.nic.titulo
    titulos_nic.short_description = 'Titulos NIC'
    def titulos_noc (self, obj):
        return '%s'%obj.noc.titulo
    titulos_noc.short_description = 'Titulos NOC'
    def prioridad_relacion (self, obj):
        return '%s'%obj.prioridad.titulo
    prioridad_relacion.short_description = 'Prioridad'
    list_display_links = ('titulos_nic','titulos_noc')

admin.site.register(noc)
admin.site.register(nocClase)
admin.site.register(nocDominio)
admin.site.register(nocEscala)
admin.site.register(nocEspecialidad)
admin.site.register(nocIndicador)
admin.site.register(relacionNandaNoc,NandaNocAdmin)
admin.site.register(relacionNicNoc, NicNocAdmin)
admin.site.register(prioridad)

__author__ = 'ehebel'
