from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from backend_api.models import Product
from backend_api.serializer import ProductSerializer

# Create your views here.


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()  # Complex Data
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def product(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return serializer.errors

    if request.method == 'DELETE':
        product.delete()
        return Response({
            'delete': True
        })
