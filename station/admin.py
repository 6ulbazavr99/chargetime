from django.contrib import admin

from .models import Station, StationImage

class StationImageInline(admin.TabularInline):
    model = StationImage
    extra = 1



@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc')
    list_display_links = ('name',)


@admin.register(StationImage)
class StationImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    inlines = [StationImageInline]