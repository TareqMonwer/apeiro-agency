from django.urls import path
from . import api_views


urlpatterns = [
    path('total-baskets/',
        api_views.get_basket_count,
        name='get_basket_count'
    ),
    path('basket-items/', api_views.BasketItemsList.as_view(),
        name='get_basket_items'
    ),
]