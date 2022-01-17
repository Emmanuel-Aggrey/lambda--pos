from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from store.models import Product
from store.serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from  store.views import  set_expire_date

@api_view(['GET', 'POST'])
def product_views(request):
    """
    LIST ALL PRODUCTS, OR CREATE A NEW PRODUCTS
    """

    if request.method == 'GET':

        product = Product.objects.all()

        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'POST', 'DELETE'])
def product_view(request, pk):
    """
    UPDATE, GET OR DELETE A PRODUCT
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = ProductSerializer(product,
                                       data=request.data,
                                       partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'POST':
        data = request.data

        # print(data)

        name = data.get('name')
        price = data.get('price')
        quantity = data.get('quantity')
        description = data.get('description')
        category = pk
        unit = data.get('unit')
        supplier = request.POST.getlist('supplier[]')
        stock_level = data.get('stock_level')
        shelf_number = data.get('shelf_number')
        has_expire_date = str( data.get('has_expire_date')).capitalize()
        months_to_expire = data.get('months_to_expire',3)
        expire_date = set_expire_date(data.get('expire_date'))

     

        # product = product
        product.name=name
        product.price=price
        product.quantity=quantity
                                         
        product.description=description
        # product.category_id=category
        product.unit_id=unit
        product.stock_level=stock_level
        product.shelf_number=shelf_number
        product.has_expire_date=has_expire_date
        product.months_to_expire=months_to_expire
        product.expire_date=expire_date
        product.supplier.set(supplier)





        product.save()

        return Response({'data':'created successfully'}, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



