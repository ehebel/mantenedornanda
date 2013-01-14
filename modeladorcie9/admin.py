from django.contrib import admin
from mantenedornanda.modeladorcie9.models import *

class cienueveAdmin(admin.ModelAdmin):
    list_display = ('codigo','descriptor','area')

class procedimientoAdmin(admin.ModelAdmin):
    list_display = ('idintervencionclinica','integlosa','grpdescripcion','grpdescripcion','codsubgrupo','sgrdescripcion','inte_codigo_fonasa')
    fields = ('idintervencionclinica','integlosa','grpdescripcion')
#    search_fields = ('integlosa',)
#    filter_vertical = ('cienueve',)
    class Meta:
        ordering=['id']


class cas_proc_descAdmin(admin.ModelAdmin):
    list_display = ('termino','idconcepto','tipodescripcion')

admin.site.register(cas_concepto)
admin.site.register(cas_descripcion)
admin.site.register(cas_conj_mapeo)
admin.site.register(cas_mapsalida)
admin.site.register(cas_mapdestino)
admin.site.register(cas_mapeo)

admin.site.register(cienueve, cienueveAdmin)
admin.site.register(cas_procedimiento,procedimientoAdmin)
admin.site.register(cas_procedimiento_desc, cas_proc_descAdmin)

__author__ = 'ehebel'