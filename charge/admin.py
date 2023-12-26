from django.contrib import admin
from .models import Column, ChargeType




@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'station')
    list_display_links = ('',)


@admin.register(ChargeType)
class ChargeTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
