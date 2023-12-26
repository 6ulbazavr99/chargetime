from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from feedback.admin import ReviewImageInline
from .models import Station, StationImage

admin.site.register(Station, LeafletGeoAdmin)
admin.site.register(StationImage, LeafletGeoAdmin)
class StationImageInline(admin.TabularInline):
    model = StationImage
    extra = 1


@admin.register(Station)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc')
    list_display_links = ('name',)
    inlines = [ReviewImageInline]


@admin.register(StationImage)
class StationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    inlines = [StationImageInline]