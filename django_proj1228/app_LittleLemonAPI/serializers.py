from rest_framework import serializers
from .models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
        'id',
        'title',
        'price',
        'inventory'
    ]



""" 1228 original longer code

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            'id',
            'title',
            'price',
            'inventory'
        ]
"""