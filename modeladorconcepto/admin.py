__author__ = 'ehebel'
from django.contrib import admin
from mantenedornanda.modeladorconcepto.models import *
from django.forms import TextInput, Textarea
import csv
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied

if 'delete_selected' in admin.site.actions:
    admin.site.disable_action('delete_selected')

def make_consultar(modeladmin, request, queryset):
    queryset.update(consultar='1')
make_consultar.short_description = 'Marcar codigos para consultar.'

def make_revisado(modeladmin, request, queryset):
    queryset.update(revisado='1')
make_revisado.short_description = 'Marcar codigos seleccionados como revisados.'

def make_norevisado(modeladmin, request, queryset):
    queryset.update(revisado='0')
make_revisado.short_description = 'Marcar codigos seleccionados como NO revisados.'

def make_ambiguo(modeladmin, request, queryset):
    queryset.update(ambiguo='1')
make_ambiguo.short_description = 'Marcar codigos seleccionados como ambiguos'

def export_as_csv(modeladmin, request, queryset):
    """
    Generic csv export admin action.
    """
    if not request.user.is_staff:
        raise PermissionDenied
    opts = modeladmin.model._meta
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')
    writer = csv.writer(response, delimiter=';')
    field_names = [field.name for field in opts.fields]
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows
    for obj in queryset:
        values = []
        for field in field_names:
            value = (getattr(obj, field))
            if callable(value):
                try:
                    value = value() or ''
                except:
                    value = 'Error retrieving value'
            if value is None:
                value = ''
            values.append(unicode(value).encode('utf-8'))
        writer.writerow(values)
        #writer.writerow([getattr(obj, field) for field in field_names])
    return response
export_as_csv.short_description = "Exportar elementos seleccionados como CSV"

class DescInline(admin.TabularInline):
    model = img_descripcione

class ConcRadInLine(admin.TabularInline):
    model = img_concepto

class RadConceptAdmin(admin.ModelAdmin):
    inlines = [DescInline,]

class radioAdmin(admin.ModelAdmin):
    list_display = ('QDoc_ExamName','observacion'
        ##            ,'revisado','consultar','no_pedible','ambiguo'
        )
    list_filter = ('revisado','consultar','no_pedible','ambiguo','Origin_File'
                   ,'QP_ExamGroupCode','QP_ExamGroupDescription'  )
    search_fields = ('QDoc_ExamName','observacion')
    readonly_fields = ('QP_ExamGroupCode','QP_ExamGroupDescription')
    actions = [export_as_csv,make_revisado,make_consultar, make_ambiguo, make_norevisado]
    #raw_id_fields = ['relacion']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'80'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        }
    inlines = [ConcRadInLine,]
    fieldsets = (
        (None, {
            'fields': ('QDoc_ExamName','QDoc_ExamName2','revisado','observacion'
                        ,'consultar','no_pedible','ambiguo','QDoc_ExamCode','Origin_File'
                        ,'QP_ExamGroupCode','QP_ExamGroupDescription'
                )
        }),
        )
    def add_view(self, request, *args, **kwargs):
        result = super(radioAdmin, self).add_view(request, *args, **kwargs )
        request.session['filtered'] =  None
        return result
    def change_view(self, request, object_id, extra_context={}):
        result = super(radioAdmin, self).change_view(request, object_id, extra_context )
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


class loincAdmin(admin.ModelAdmin):
    list_filter = ('_class',)


class loincMapAdmin(admin.ModelAdmin):
    def codigos_loinc(self, obj):
        return '%s'%obj.loinc.component
    codigos_loinc.short_description = 'Codigos Loinc'
    def codigos_mapeo(self, obj):
        return '%s'%obj.loinc.loinc_num
    codigos_mapeo.short_description = 'Codigos de Mapeo'
    list_display = ('id','codigos_loinc','codigos_mapeo')
    class Meta:
        ordering = ['id']


admin.site.register(Loinc, loincAdmin)
admin.site.register(Loinc_source_organization)
admin.site.register(Loinc_map_to,loincMapAdmin)
admin.site.register(Sct_concept)
admin.site.register(Sct_description)
admin.site.register(Sct_relationship)
admin.site.register(img_concepto,RadConceptAdmin)
admin.site.register(img_descripcione)
admin.site.register(radiologico,radioAdmin)
