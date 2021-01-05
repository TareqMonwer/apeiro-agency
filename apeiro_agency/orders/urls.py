from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.add_to_basket,
        name='add_to_basket'
    ),
    path('cart/', views.manage_basket,
        name='cart'
    ),
]

