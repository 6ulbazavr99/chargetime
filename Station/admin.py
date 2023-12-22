from django.contrib import admin
from .models import Review, Rating, ReviewImage, Station, Column, ChargeType

admin.site.register(Station)
admin.site.register(Column)
admin.site.register(ChargeType)

class ReviewImageInline(admin.TabularInline):
    model = ReviewImage
    extra = 1


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'station')
    list_display_links = ('author',)
    inlines = [ReviewImageInline]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'rating')
    list_display_links = ('author',)




# Register your models here.
