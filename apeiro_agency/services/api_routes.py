from django.urls import path

from . import api_views


urlpatterns = [
    path(
        'category/<int:pk>/',
        api_views.CategoryDetailAPIView.as_view(),
        name='category'
    ),
]
