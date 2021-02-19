from model_utils.models import TimeStampedModel

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from core.models import FeatureItem, PricingPlan
from service_analytics.models import Impression


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
            'services:category_service_list',
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
    slug = models.SlugField(blank=True, null=True, unique=True)
    primary_image = models.ImageField(
        upload_to='services/primary-images/',
        blank=True,
        default='services/primary-images/default.jpg'
    )
    description = models.TextField(blank=True, null=True)
    vendor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='services',
        on_delete=models.CASCADE
    )
    features = models.ManyToManyField(
        FeatureItem,
        blank=True
    )
    pricing = models.ForeignKey(
        PricingPlan,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name='services'
    )
    is_verified = models.BooleanField(default=False)

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


class ServicePhoto(TimeStampedModel):
    image = models.ImageField(upload_to='services/images/')
    service = models.ForeignKey(Service,
        related_name='images',
        on_delete=models.CASCADE
    )