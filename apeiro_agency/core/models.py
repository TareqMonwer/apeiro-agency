from model_utils.models import TimeStampedModel

from django.db import models
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


class ServiceCategory(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    category_icon = models.ImageField(
        upload_to='category_icons/',
        default='category_icons/default.png'
    )
    image = models.ImageField(
        upload_to='category/',
        default='category/default.jpg'
    )
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['name', '-created']
        verbose_name_plural = 'Service Categories'
        
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        update = kwargs.get('update', False)
        if not update:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Service(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(
        upload_to='service_icons/',
        default='service_icons/default.png'
    )
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField(blank=True, null=True)
    features = models.ManyToManyField(FeatureItem)
    pricing = models.ForeignKey(
        PricingPlan,
        on_delete=models.CASCADE,
        related_name='services'
    )
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name='services'
    )

    class Meta:
        ordering = ['name', '-created']
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        update = kwargs.get('update', False)
        if not update:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

