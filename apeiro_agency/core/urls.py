from django.urls import path
from . import views

app_name = 'core'

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
        "category/<slug:slug>/",
        views.category_detail_view,
        name='category_detail'
    )
]

