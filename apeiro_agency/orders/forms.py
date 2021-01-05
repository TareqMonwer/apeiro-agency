from django.forms import inlineformset_factory
from .models import Basket, BasketLine


basketline_formset = inlineformset_factory(
    Basket,
    BasketLine,
    fields=('quantity',),
    extra=0
)