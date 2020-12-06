from django.contrib import admin
from .models import County, HeadOffice, RegionalOffice, FieldOffice
from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin


class OfficeAdmin(LeafletGeoAdmin):
    list_display = ('title', 'designation', 'area_of_coverage',
                    'physical_features', 'number_of_staff', 'issues_addressed',
                    'location')
    search_fields = ('title', )
    filter_fields = ('title', 'location')


class HeadOfficeAdmin(LeafletGeoAdmin):
    list_display = ('title', 'designation', 'area_of_coverage',
                    'physical_features', 'number_of_staff', 'issues_addressed',
                    'location')
    search_fields = ('title', )
    filter_fields = ('title', 'location')


class CountyAdmin(LeafletGeoAdmin):
    list_display = ('name', 'city_code')
    search_fields = ('name', )
    filter_fields = ('name', 'city_code')


admin.site.register(HeadOffice, HeadOfficeAdmin)
admin.site.register(RegionalOffice, OfficeAdmin)
admin.site.register(FieldOffice, OfficeAdmin)
admin.site.register(County, CountyAdmin)
