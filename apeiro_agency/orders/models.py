from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings

from core.models import Service


class Basket(models.Model):
    OPEN = 10
    SUBMITTED = 20
    STATUSES = (
        (OPEN, "Open"),
        (SUBMITTED, "Submitted")
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    status = models.IntegerField(
        choices=STATUSES,
        default=OPEN
    )

    def is_empty(self):
        return self.basketline_set.all().count() == 0

    def count(self):
        return sum(i.quantity for i in self.basketline_set.all())


class BasketLine(models.Model):
    basket = models.ForeignKey(
        Basket,
        on_delete=models.CASCADE
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )
