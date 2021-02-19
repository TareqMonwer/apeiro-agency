from django.contrib import admin
from .models import Service, ServiceCategory


@admin.register(ServiceCategory)
class AdminServiceCategory(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created', 'is_featured')
    list_editable = ('is_featured', )


@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ('name', 'pricing',)
