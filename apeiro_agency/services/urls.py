from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path(
        "",
        views.home_page_view,
        name="home",
    ),
    path(
        "categories/",
        views.category_list_view,
        name='category_list'
    ),
    path(
        "services/",
        views.service_list_view,
        name='service_list'
    ),
    path(
        "services/<slug:category>/",
        views.service_list_view,
        name='category_service_list'
    ),
]

