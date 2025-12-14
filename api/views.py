from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ProductListCreate(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        incoming = request.data.get('fields')
        
        if not isinstance(incoming, dict):
            return Response(
                {"fields": "This field is required and must be an object (not NULL)."},
                status=status.HTTP_400_BAD_REQUEST
            )

        
        current = instance.data or {}

        
        current.update(incoming)

        instance.data = current
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
