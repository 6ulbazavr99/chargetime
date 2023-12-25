from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Station, StationImage

admin.site.register(Station, LeafletGeoAdmin)
admin.site.register(StationImage, LeafletGeoAdmin)
