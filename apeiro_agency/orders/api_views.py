from django.http import JsonResponse


def get_basket_count(request):
    basket_count = request.basket.count() if request.basket else 0
    print(basket_count)
    return JsonResponse({'basket_count': basket_count})