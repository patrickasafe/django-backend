from django.shortcuts import render
from django.http import JsonResponse
from backend.models import Product

# Create your views here.


def product_list(request):
    products = Product.objects.all()  # Complex Data
    products_python = list(products.values())  # Python DS
    return JsonResponse({
        'books': products_python
    })
