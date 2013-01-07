from django.shortcuts import render_to_response
from django.http import Http404

from mantenedornanda.mantnandaapp.models import nanda


def lista_nandas(solicitud):
    nandas = nanda.objects.order_by('id')
    return render_to_response('lista_nandas.html',{'listado_nandas':nandas})

def selec_nanda(solicitud, nandaid):
    try:
        nandaid = int(nandaid)
    except ValueError:
        raise Http404
    nandas = nanda.objects.order_by('id').get(id=nandaid)
    nandaclases = nandas.nandaclase_set.all()
    caract = nandas.nandacaracteristica_set.all()
    nandanic = nandas.relacionnandanic_set.all()
    nandanoc = nandas.relacionnandanoc_set.all()
    return render_to_response('seleccion_nanda.html'
        ,{'listado_clases':nandaclases
        ,'listado_caract':caract
        ,'selec_nanda':nandas
        ,'nandanic':nandanic
        ,'nandanoc':nandanoc
        })