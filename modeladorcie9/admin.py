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
                    ,'sgrdescripcion','inte_codigo_fonasa','revisado','consultar')
    readonly_fields = ('idintervencionclinica','integlosa','codgrupo'
                       ,'grpdescripcion','codsubgrupo','sgrdescripcion'
                       ,'inte_codigo_fonasa')
    filter_horizontal = ('cienueve')
    #raw_id_fields = ('cienueve',)
    list_filter = ('revisado','incodificable','consultar','grpdescripcion','sgrdescripcion')
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
    def add_view(self, request, *args, **kwargs):
        result = super(procedimientoAdmin, self).add_view(request, *args, **kwargs )
        request.session['filtered'] =  None
        return result
    def change_view(self, request, object_id, extra_context={}):
        result = super(procedimientoAdmin, self).change_view(request, object_id, extra_context )
        ref = request.META.get('HTTP_REFERER', '')
        if ref.find('?') != -1:
            request.session['filtered'] =  ref

        if request.POST.has_key('_save'):
            try:
                if request.session['filtered'] is not None:
                    result['Location'] = request.session['filtered']
                    request.session['filtered'] = None
            except:
                pass
        return result
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
    list_display = ('descriptionid_vmp','vmp','arsenal','revisado','consultar')
    list_filter = ('revisado','arsenal','consultar','desconocido','cambio_nombre','vtm')
    readonly_fields = ('descriptionid_vmp','vmp','descriptionid_vtm', 'vtm')
    search_fields = ('vtm','vmp')
    filter_vertical = ('dbnet','kairos')
    fieldsets = (
        (None, {
            'fields': ('vtm','descriptionid_vmp', 'vmp', 'revisado', 'arsenal','consultar','desconocido'
                       ,'cambio_nombre','observacion','dbnet','kairos')
        }),
        )
    def add_view(self, request, *args, **kwargs):
        result = super(cas_termAdmin, self).add_view(request, *args, **kwargs )
        request.session['filtered'] =  None
        return result
    def change_view(self, request, object_id, extra_context={}):
        result = super(cas_termAdmin, self).change_view(request, object_id, extra_context )
        ref = request.META.get('HTTP_REFERER', '')
        if ref.find('?') != -1:
            request.session['filtered'] =  ref
        if request.POST.has_key('_save'):
            try:
                if request.session['filtered'] is not None:
                    result['Location'] = request.session['filtered']
                    request.session['filtered'] = None
            except:
                pass
        return result
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        }


class dbnetprodAdmin(admin.ModelAdmin):
    list_display = ('codigo','producto','cod_principio_activo','cod_acc_farmacologica')
    list_filter = ('cod_principio_activo','cod_acc_farmacologica')
    search_fields = ('producto',)


class kairosproductosAdmin(admin.ModelAdmin):
    list_display = ('productos_descripcion','concentracion','unidadconcentracion','medio','cantidadenvase','abreviatura')
    list_filter = ('medio','abreviatura')
    search_fields = ('productos_descripcion','abreviatura','laboratorios_descripcion')


admin.site.register(cas_concepto)
admin.site.register(cas_descripcion)
admin.site.register(cas_conj_mapeo)
admin.site.register(cas_mapsalida)
admin.site.register(cas_mapdestino)
admin.site.register(cas_mapeo)
admin.site.register(ciediez)
admin.site.register(cas_dbnet_ppio_activo)
admin.site.register(cas_dbnet_ax_farmacol)
admin.site.register(cas_kairos_ax_terapeut)
admin.site.register(cas_kairos_sustancia)
admin.site.register(cas_kairos_relacion_producto_ax)
admin.site.register(cas_kairos_relacion_producto_sustancia)

admin.site.register(cienueve, cienueveAdmin)
admin.site.register(cas_procedimiento,procedimientoAdmin)
admin.site.register(cas_procedimiento_desc, cas_proc_descAdmin)
admin.site.register(cas_procedimiento_cienueve, relacionProcCieAdmin)
admin.site.register(cas_dbnet_producto,dbnetprodAdmin)
admin.site.register(cas_kairos_producto,kairosproductosAdmin)
admin.site.register(cas_term_vtm_vmp, cas_termAdmin)


__author__ = 'ehebel'

