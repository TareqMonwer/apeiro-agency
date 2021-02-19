from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)

from .models import ServiceCategory, Service


class HomePageView(TemplateView):
    template_name = 'services/home.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        featured_categories = ServiceCategory.objects.filter(
            is_featured=True
        )
        ctx['featured_categories'] = featured_categories
        return ctx

home_page_view = HomePageView.as_view()


class ServiceListView(TemplateResponseMixin, View):
    model = Service
    template_name = 'services/products.html'

    def get(self, request, category=None):
        categories = ServiceCategory.objects.annotate(
            total_services=Count('services'))
        services = Service.objects.all()

        if category:
            category = get_object_or_404(ServiceCategory, slug=category)
            services = services.filter(category=category)
        return self.render_to_response({
            'categories': categories,
            'category': category,
            'services': services
        })

service_list_view = ServiceListView.as_view()

class CategoryListView(ListView):
    model = ServiceCategory
    template_name = 'services/category_list.html'
    context_object_name = 'categories'

category_list_view = CategoryListView.as_view()


class CategoryDetailView(DetailView):
    model = ServiceCategory
    template_name = 'services/category_detail.html'
    context_object_name = 'category'
    slug_field = 'slug' 
    slug_url_kwarg = 'slug' 

category_detail_view = CategoryDetailView.as_view()
