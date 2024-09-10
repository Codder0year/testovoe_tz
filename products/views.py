from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def products_page(request):
    return render(request, 'products/products.html')