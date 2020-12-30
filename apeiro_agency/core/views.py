from django.shortcuts import render
from django.views.generic import TemplateView

from .models import ServiceCategory


class HomePageView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        featured_categories = ServiceCategory.objects.filter(
            is_featured=True
        )
        ctx['featured_categories'] = featured_categories
        return ctx

home_page_view = HomePageView.as_view()
