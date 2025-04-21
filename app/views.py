from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Product, Category
from app.serializers import ProductSerializer, CategorySerializer


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Products': {
            'List': '/api/products/',
            'Create': '/api/products/create/',
            'Update': '/api/products/<int:pk>/update/',
            'Delete': '/api/products/<int:pk>/delete/', },
        'Categories': {
            'List': '/api/categories/',
            'Create': '/api/categories/create/',
            'Update': '/api/categories/<int:pk>/update/',
            'Delete': '/api/categories/<int:pk>/delete/',
        }
    }

    return Response(api_urls)

# ========== PRODUCT CRUD ==========


@api_view(['GET'])
def product_list(request):
    if request.query_params:
        products = Product.objects.filter(**request.query_params.dict())
    else:
        products = Product.objects.all()

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return Response({"message": "Product deleted."}, status=status.HTTP_202_ACCEPTED)


# ========== CATEGORY CRUD ==========

@api_view(['PUT'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def category_create(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(instance=category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return Response({"message": "Category deleted."}, status=status.HTTP_202_ACCEPTED)
