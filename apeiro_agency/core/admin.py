from django.contrib import admin

from .models import (
    ServiceCategory,
    Service,
    FeatureItem,
    PricingPlan
)


@admin.register(ServiceCategory)
class AdminServiceCategory(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created', 'is_featured')
    list_editable = ('is_featured', )


@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ('name', 'pricing',)


@admin.register(FeatureItem)
class AdminFeatureItem(admin.ModelAdmin):
    list_display = ('feature_key', 'feature',)


@admin.register(PricingPlan)
class AdminPricingPlan(admin.ModelAdmin):
    list_display = (
        'title', 'monthly_price',
        'annual_price', 'ontime_pay'
    )
