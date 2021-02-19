from model_utils.models import TimeStampedModel

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class PricingPlan(TimeStampedModel):
    title = models.CharField(max_length=50)
    monthly_price = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    annual_price = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    ontime_pay = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('title',)

    def __str__(self):
        s = f'{self.title}, '
        if self.monthly_price:
            s += f'monthly: {self.monthly_price} '
        if self.annual_price:
            s += f'annual: {self.annual_price} '
        if self.ontime_pay:
            s += f'onetime: {self.ontime_pay}'
        return s.strip()


class FeatureItem(TimeStampedModel):
    feature_key = models.CharField(max_length=200)
    feature = models.CharField(max_length=200)

    class Meta:
        ordering = ('feature_key',)

    def __str__(self):
        return f'{self.feature_key} : {self.feature}'
