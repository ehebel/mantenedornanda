from django.contrib import admin
from mantenedornanda.modeladorcie9.models import *

class cienueveAdmin(admin.ModelAdmin):
    list_display = ('codigo','descriptor','area')
    search_fields = ('descriptor','codigo')
    list_filter = ('area','clasificacion')

class procedimientoAdmin(admin.ModelAdmin):
    list_display = ('idintervencionclinica','integlosa','grpdescripcion','codsubgrupo','sgrdescripcion','inte_codigo_fonasa','revisado')
    readonly_fields = ('idintervencionclinica','integlosa','codgrupo'
                       ,'grpdescripcion','codsubgrupo','sgrdescripcion'
                       ,'inte_codigo_fonasa')
    raw_id_fields = ('cienueve',)
    list_filter = ('revisado',)
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