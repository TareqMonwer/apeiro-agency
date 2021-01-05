from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from core.models import Service
from .models import Basket, BasketLine
from .forms import basketline_formset


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
    return JsonResponse({'status': 1})


def manage_basket(request):
    if not request.basket or request.basket.is_empty():
        return render(request, 'orders/basket.html', {'formset': None})
    
    if request.method == 'POST':
        formset = basketline_formset(
            request.POST, instance=request.basket,
        )
        if formset.is_valid():
            formset.save()
    else:
        formset = basketline_formset(
            instance=request.basket,
        )
    
    return  render(request, 'orders/basket.html', {'formset': formset})