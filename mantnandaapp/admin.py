from django.contrib import admin
from mantenedornanda.mantnandaapp.models import nanda, nandaClase, nandaDominio, nandaCaracteristica, nandaTipo,nandaValoracion
from django.forms import TextInput, Textarea
from django.db import models

class nandaAdmin(admin.ModelAdmin):
    fields = ('numero','titulo','definicion','edicion','tituloabreviado','observacion','revisado')
    readonly_fields = ('numero','titulo','definicion','edicion')
    list_display = ('numero','titulo','revisado')
    search_fields = ('titulo', 'definicion')
    list_filter = ('revisado',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'60'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        }

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance,'usrmodificacion'):
            instance.usrmodificacion = request.user
        instance.usrmodificacion = request.user
        instance.save()
        form.save_m2m()
        return instance

    def save_formset(self, request, form, formset, change):

        def set_user(instance):
            if not instance.usrmodificacion:
                instance.usrmodificacion = request.user
            instance.usrmodificacion = request.user
            instance.save()

        if formset.model == nanda:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()


class nandaDominioAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','descripcion')
    ordering = ('id',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'60'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        }

class nandaClaseAdmin(admin.ModelAdmin):
    field_hierarchy = ('dominio')
    search_fields = ('titulo',)
    filter_vertical = ('nanda',)

class nandaCaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('id',)
#    list_display = ('id','titulo','tipo','subtipo',)
#    search_fields = ('titulo',)
#    list_filter = ('tipo',)

class nandaValoracionAdmin(admin.ModelAdmin):
    filter_vertical = ('nanda',)

admin.site.register(nanda,nandaAdmin)
admin.site.register(nandaClase, nandaClaseAdmin)
admin.site.register(nandaDominio, nandaDominioAdmin)
admin.site.register(nandaCaracteristica,nandaCaracteristicaAdmin)
admin.site.register(nandaTipo)
admin.site.register(nandaValoracion,nandaValoracionAdmin)
__author__ = 'ehebel'
