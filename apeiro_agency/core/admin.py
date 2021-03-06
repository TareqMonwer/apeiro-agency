from django.contrib import admin

from .models import (
    FeatureItem,
    PricingPlan
)


@admin.register(FeatureItem)
class AdminFeatureItem(admin.ModelAdmin):
    list_display = ('feature_key', 'feature',)


@admin.register(PricingPlan)
class AdminPricingPlan(admin.ModelAdmin):
    list_display = (
        'title', 'monthly_price',
        'annual_price', 'ontime_pay'
    )
