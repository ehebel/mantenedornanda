from django.contrib import admin
from mantenedornanda.modeladorcie9.models import *

class cienueveAdmin(admin.ModelAdmin):
    list_display = ('codigo','descriptor','area')

class procedimientoAdmin(admin.ModelAdmin):
    search_fields = ('grpdescripcion',)
    filter_vertical = ('cienueve',)

admin.site.register(cas_concepto)
admin.site.register(cas_descripcion)
admin.site.register(cas_conj_mapeo)
admin.site.register(cas_mapsalida)
admin.site.register(cas_mapdestino)
admin.site.register(cas_mapeo)


admin.site.register(cienueve, cienueveAdmin)
admin.site.register(cas_procedimiento,procedimientoAdmin)
__author__ = 'ehebel'