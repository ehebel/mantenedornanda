import autocomplete_light

from modeladorges.models import ciediez

autocomplete_light.register(ciediez, search_fields=('^descriptor',),
    autocomplete_js_attributes={'placeholder': 'diagnostico ..'})

__author__ = 'ehebel'
