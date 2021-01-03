from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from core.models import Service
from .models import Basket, BasketLine



def add_to_basket(request):
    service = get_object_or_404(
        Service, pk=request.GET.get('service_id')
    )
    basket = request.basket
    if not request.basket:
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        basket = Basket.objects.create(
            user=user,
        )
        request.session['basket_id'] = basket.id
    basketline, created = BasketLine.objects.get_or_create(
        basket=basket, service=service
    )   

    if not created:
        basketline.quantity = 1
        basketline.save()
    return HttpResponseRedirect(reverse('service', args=(product.slug, )))