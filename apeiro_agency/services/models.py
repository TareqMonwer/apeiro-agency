from model_utils.models import TimeStampedModel

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from core.models import FeatureItem, PricingPlan


class ServiceCategory(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    category_icon = models.ImageField(
        upload_to='category_icons/',
        blank=True,
        default='category_icons/default.png'
    )
    image = models.ImageField(
        upload_to='category/',
        blank=True,
        default='category/default.jpg'
    )
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['name', '-created']
        verbose_name_plural = 'Service Categories'
    
    def get_absolute_url(self):
        return reverse(
            'services:category_detail',
            args=(),
            kwargs={'slug': self.slug}
        )    
    
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
    features = models.ManyToManyField(
        FeatureItem,
        blank=True,
        null=True
    )
    pricing = models.ForeignKey(
        PricingPlan,
        on_delete=models.CASCADE,
        related_name='services',
        blank=True,
        null=True
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

