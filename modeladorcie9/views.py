from django.shortcuts import render_to_response
from django.http import Http404

from mantenedornanda.modeladorcie9.models import cas_procedimiento

def list_cas_proc(solicitud):
    procedimientos = cas_procedimiento.objects.order_by('id')
    return render_to_response('lista_cas_cie.html'
        ,{'listado_proc':procedimientos}
    )