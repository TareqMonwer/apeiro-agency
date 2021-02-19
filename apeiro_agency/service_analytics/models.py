from model_utils.models import TimeStampedModel

from django.db import models
from django.conf import settings


class Impression(TimeStampedModel):
    interested_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True
    )
    service = models.ForeignKey(
        "services.Service",
        on_delete=models.CASCADE,
        related_name='impressions'
    )
    count = models.BigIntegerField(default=0)


class Rating(TimeStampedModel):
    RATING_VALUES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ) 
    service = models.ForeignKey(
        "services.Service",
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    value = models.SmallIntegerField(choices=RATING_VALUES)
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


class Sell(TimeStampedModel):
    service = models.ForeignKey(
        "services.Service",
        on_delete=models.CASCADE,
        related_name='sells'
    )
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='purchases'
    )