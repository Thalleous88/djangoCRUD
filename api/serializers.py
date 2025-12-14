from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    fields = serializers.JSONField(source='data')
    required = True

    class Meta:
        model = Product
        fields = ['id', 'fields'] 