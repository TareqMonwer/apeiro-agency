from django.contrib import admin

from .models import Impression, Rating, Sell

@admin.register(Impression)
class ImporessionAdmin(admin.ModelAdmin):
    list_display = ('count', )


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('service', 'value', 'customer')


@admin.register(Sell)
class SellAdmin(admin.ModelAdmin):
    list_display = ('service', 'customer')