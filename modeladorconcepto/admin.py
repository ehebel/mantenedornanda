__author__ = 'ehebel'
from django.contrib import admin
from mantenedornanda.modeladorconcepto.models import *

import csv
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied


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


class radioAdmin(admin.ModelAdmin):
    list_display = ('QP_ExamCode','QDoc_ExamCode','QDoc_ExamName'
                    ,'revisado','consultar','no_pedible','ambiguo')
    list_filter = ('revisado','consultar','no_pedible','ambiguo'
                   ,'QP_ExamGroupCode','QP_ExamGroupDescription'  )
    actions = [export_as_csv]

admin.site.register(radiologico,radioAdmin)