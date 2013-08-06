from django.contrib import admin
import autocomplete_light
autocomplete_light.autodiscover()

from mantenedornanda.modeladorges.models import *


class gesAdmin(admin.ModelAdmin):
    form = gesAdminForm
admin.site.register(ges_patologia, gesAdmin)

__author__ = 'ehebel'

