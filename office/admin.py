from django.contrib import admin
from .models import Incidence


class IncidenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_reported', 'location')
    search_fields = ('title', )
    filter_fields = ('title', 'date_reported')


admin.site.register(Incidence, IncidenceAdmin)
