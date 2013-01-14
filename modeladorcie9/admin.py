from django.contrib import admin
from mantenedornanda.modeladorcie9.models import *

class cienueveAdmin(admin.ModelAdmin):
    list_display = ('codigo','descriptor','area')

class procedimientoAdmin(admin.ModelAdmin):
    list_display = ('idintervencionclinica','integlosa','grpdescripcion')
    fields = ('idintervencionclinica','integlosa','grpdescripcion')
#    search_fields = ('integlosa',)
#    filter_vertical = ('cienueve',)
    def __unicode__(self):
        return self.integlosa
    class Meta:
        ordering=['id']


admin.site.register(cas_concepto)
admin.site.register(cas_descripcion)
admin.site.register(cas_conj_mapeo)
admin.site.register(cas_mapsalida)
admin.site.register(cas_mapdestino)
admin.site.register(cas_mapeo)

admin.site.register(cienueve, cienueveAdmin)
admin.site.register(cas_procedimiento,procedimientoAdmin)
admin.site.register(cas_procedimiento_desc)

__author__ = 'ehebel'