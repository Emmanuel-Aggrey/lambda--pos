
from  django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

# Create your views here.
from store.serializers import (CategorySerializer, GenericSerializer,
                               ProductSerializer)

from .models import Generic, Category, Product


# reqgular view to return all products in hierrachical order
def all_products(request):
    category = Category.objects.all()

    context ={
        'category':category,
    }
    return render(request,'reports/products_all.html',context)


@api_view(['GET', 'POST'])
def categories_in_generics(request, pk):
    """
    GET CATEGORIES IN SAME GENERIC MODEL
    """
    try:
        category = Category.objects.filter(generic_id=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        name = request.POST.get('name')
        description = request.POST.get('description')

        category = Category.objects.create(
            name=name, description=description, generic_id=pk)
        # if not saving then unique constraints error

        return Response({'data', 'created'}, status=status.HTTP_201_CREATED)

        # not able to save to category with GENERIC object
        # serializer = CategorySerializer(data=request.data)
        # if serializer.is_valid():

        #     serializer.save()
        # if serializer.errors:
        #     # print(serializer.errors)
        #     return Response(serializer.data)
        # return Response(serializer.errors,
        #                 status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def products_in_category(request, pk):
    """
    GET PRODUCTS IN SAME CATEGORY MODEL
    """
    try:
        product = Product.objects.filter(category_id=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        product = product.filter(category=pk).first()
        data = request.data

        name = data.get('name')
        price = data.get('price',)
        quantity = data.get('quantity')
        description = data.get('description')
        category = pk
        unit = data.get('unit')
        supplier = request.POST.getlist('supplier[]')
        stock_level = data.get('stock_level')
        shelf_number = data.get('shelf_number')
        months_to_expire = data.get('months_to_expire',3)

        has_expire_date = str( data.get('has_expire_date')).capitalize()
        expire_date = set_expire_date(data.get('expire_date'))

        print('expire_date',expire_date,months_to_expire)

        product = Product.objects.create(name=name, price=price, quantity=quantity,
                                         description=description, category_id=category, unit_id=unit,
                                         stock_level=stock_level, shelf_number=shelf_number,
                                         has_expire_date=has_expire_date,months_to_expire=months_to_expire, expire_date=expire_date)
        product.supplier.set(supplier)

        return Response({'data':'created successfully'}, status=status.HTTP_201_CREATED)


def set_expire_date(date):
    if date:
        return date
    else:
        return None