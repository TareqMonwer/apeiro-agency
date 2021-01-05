from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.generics import RetrieveAPIView, ListAPIView

from .serializers import BasketLineSerializer


def get_basket_count(request):
    basket_count = request.basket.count() if request.basket else 0
    return JsonResponse({'basket_count': basket_count})


# def get_basket_items(request):
#     basket = request.basket
    
#     basketlines = serializers.serialize('json', basket.basketlines.all())
#     print(basketlines)
#     if basket:
#         return JsonResponse({'basket': basketlines})
#     else:
#         return JsonResponse({'basket': None})

class BasketItemsList(ListAPIView):
    serializer_class = BasketLineSerializer
    
    def get_queryset(self):
        basket = self.request.basket
        return basket.basketlines.all()