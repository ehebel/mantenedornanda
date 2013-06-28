__author__ = 'ehebel'
from django.contrib import admin
from mantenedornanda.modeladorges.models import *


class gesAdmin(admin.ModelAdmin):
    filter_horizontal = ['ciediez','casdiag','casproc']


admin.site.register(ges_patologia, gesAdmin)