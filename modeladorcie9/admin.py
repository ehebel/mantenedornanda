from django.contrib import admin
from mantenedornanda.modeladorcie9.models import *

class cienueveAdmin(admin.ModelAdmin):
    list_display = ('codigo','descriptor','area')

class procedimientoAdmin(admin.ModelAdmin):
    list_display = ('idintervencionclinica','integlosa','grpdescripcion','codsubgrupo','sgrdescripcion','inte_codigo_fonasa')
    fields = ('idintervencionclinica','integlosa','grpdescripcion')
#    search_fields = ('integlosa',)
#    filter_vertical = ('cienueve',)
    class Meta:
        ordering=['id']


class cas_proc_descAdmin(admin.ModelAdmin):
    list_display = ('termino','idconcepto','tipodescripcion')

class relacionProcCieAdmin(admin.ModelAdmin):
    list_display = ('titulos_proc','titulos_cienueve')
    def titulos_proc(self, obj):
        return '%s'%obj.cas_procedimiento.integlosa
    titulos_proc.short_description = 'Titulos Procedimientos'
    def titulos_cienueve(self, obj):
        return '%s'%obj.cienueve.descriptor
    titulos_cienueve.short_description = 'Titulos Cie-9'
    #list_display_links = ('titulos_proc','titulos_cienueve')
    #fields = ('titulos_proc','titulos_cienueve')
    #search_fields = ('titulos_proc',)                          #No lo puedo hacer funcionar
    raw_id_fields = ('cienueve',)
    class Meta:
        ordering = ['cas_procedimiento_id','id']


admin.site.register(cas_concepto)
admin.site.register(cas_descripcion)
admin.site.register(cas_conj_mapeo)
admin.site.register(cas_mapsalida)
admin.site.register(cas_mapdestino)
admin.site.register(cas_mapeo)

admin.site.register(cienueve, cienueveAdmin)
admin.site.register(cas_procedimiento,procedimientoAdmin)
admin.site.register(cas_procedimiento_desc, cas_proc_descAdmin)
admin.site.register(cas_procedimiento_cienueve, relacionProcCieAdmin)


__author__ = 'ehebel'