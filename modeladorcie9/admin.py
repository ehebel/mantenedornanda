from django.contrib import admin
from mantenedornanda.modeladorcie9.models import *
from django.forms import Textarea, TextInput

admin.site.disable_action('delete_selected')

def make_incodificable(modeladmin, request, queryset):
     queryset.update(incodificable='1')
make_incodificable.short_description = 'Marcar codigos seleccionados como incodificables.'

def make_revisado(modeladmin, request, queryset):
    queryset.update(revisado='1')
make_revisado.short_description = 'Marcar codigos seleccionados como revisados.'

class cienueveAdmin(admin.ModelAdmin):
    list_display = ('codigo','descriptor','area')
    search_fields = ('descriptor','codigo')
    list_filter = ('area','clasificacion')

class procedimientoAdmin(admin.ModelAdmin):
    list_display = ('idintervencionclinica','integlosa','grpdescripcion','codsubgrupo'
                    ,'sgrdescripcion','inte_codigo_fonasa','revisado')
    readonly_fields = ('idintervencionclinica','integlosa','codgrupo'
                       ,'grpdescripcion','codsubgrupo','sgrdescripcion'
                       ,'inte_codigo_fonasa')
    raw_id_fields = ('cienueve',)
    list_filter = ('revisado','incodificable','incodificable','grpdescripcion','sgrdescripcion')
    actions = [make_incodificable,make_revisado]
    def make_incodificable(self, request, queryset):
        queryset.update(incodificable='1')
    make_incodificable.short_description = 'Marcar codigos seleccionados como incodificables.'
    def make_revisado(self, request, queryset):
        rows_updated = queryset.update(revisado='1')
        if rows_updated == 1:
            message_bit = "Un codigo fue"
        else:
            message_bit = "%s codigos fueron" % rows_updated
        self.message_user(request, "%s exitosamente revisado(s)." % message_bit)
    make_revisado.short_description = "Marcar codigos seleccionados como revisados."
    class Meta:
        ordering=['idintervencionclinica']


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

class cas_termAdmin(admin.ModelAdmin):
    list_display = ('descriptionid_vtm','vtm','descriptionid_vmp','vmp','arsenal','revisado')
    list_filter = ('revisado','arsenal','consultar','desconocido','cambio_nombre')
    search_fields = ('vtm','vmp')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        }

class dbnetprodAdmin(admin.ModelAdmin):
    list_display = ('codigo','producto','cod_principio_activo','principio_activo')
    list_filter = ('revisado','consultar')
    search_fields = ('producto','cod_principio_activo')


admin.site.register(cas_concepto)
admin.site.register(cas_descripcion)
admin.site.register(cas_conj_mapeo)
admin.site.register(cas_mapsalida)
admin.site.register(cas_mapdestino)
admin.site.register(cas_mapeo)
admin.site.register(ciediez)
admin.site.register(cas_dbnet_producto)
admin.site.register(cas_dbnet_ppio_activo)
admin.site.register(cas_dbnet_ax_farmacol)
admin.site.register(cas_kairos_producto)
admin.site.register(cas_kairos_ax_terapeut)
admin.site.register(cas_kairos_sustancia)
admin.site.register(cas_kairos_relacion_producto_ax)
admin.site.register(cas_kairos_relacion_producto_sustancia)

admin.site.register(cienueve, cienueveAdmin)
admin.site.register(cas_procedimiento,procedimientoAdmin)
admin.site.register(cas_procedimiento_desc, cas_proc_descAdmin)
admin.site.register(cas_procedimiento_cienueve, relacionProcCieAdmin)
admin.site.register(cas_dbnet_producto,dbnetprodAdmin)
admin.site.register(cas_term_vtm_vmp, cas_termAdmin)


__author__ = 'ehebel'