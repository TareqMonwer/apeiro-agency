from django.contrib import admin
from .models import Service, ServiceCategory, ServicePhoto


@admin.register(ServiceCategory)
class AdminServiceCategory(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'is_featured')
    list_editable = ('is_featured', )


@admin.register(Service)
class AdminService(admin.ModelAdmin):

    def impression_count(self, obj):
        impressions = obj.impressions.all()
        return sum(impression.count for impression in impressions)
    impression_count.short_description = 'Total impressions'

    list_display = ('id', 'name', 'vendor', 'created',
        'is_verified', 'impression_count'
    )
    list_editable = ('is_verified', )


@admin.register(ServicePhoto)
class ServicePhoto(admin.ModelAdmin):
    list_display = ('service', )