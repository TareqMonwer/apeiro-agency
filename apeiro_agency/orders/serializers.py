from rest_framework import serializers
from .models import Basket, BasketLine


class BasketLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketLine
        fields = ['pk', 'basket', 'service']
        depth = 1