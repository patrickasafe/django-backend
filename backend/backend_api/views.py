# from rest_framework.decorators import api_view

# # from django.shortcuts import render

# # Create your views here.


# @api_view(['GET'])
# def product_list(request):


# @api_view(['POST'])
# def product_create(request):


# @api_view(['GET', 'PUT', 'DELETE'])
# def product(request, pk):


#     if request.method == 'GET':


#     if request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework.views import APIView
from backend_api.models import Product
from backend_api.serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework import status


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()  # Complex Data
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        return Response({'hello': 'friend'})


class ProductCreate(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ProductDetail(APIView):
    def get_product_by_pk(self, pk):
        try:
            product = Product.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Product does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        product = self.get_product_by_pk(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        if request.method == 'PUT':
            serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
