from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.models import Product
import requests
from django.http import JsonResponse 
from cart.cart import Cart


@api_view(['POST'])
def cart_add(request):
    '''
    ADD ITEM TO CART
    '''
    cart = Cart(request)
    data = request.data
    product = data.get('id')
    price = '{:.2f}'.format(float(data['price']))
    price = eval(price)
    quantity = int(data['quantity'])
    update_quantity = eval(data.get('update_quantity', 'False').title())

    print(type(update_quantity),update_quantity)
    cart.add(product=product, price=price,
             quantity=quantity, update_quantity=update_quantity)

    # res = requests.get('http://127.0.0.1:8000/cart/')

    # print(res.status_code)

    data = {
        "product": product,
        "price": f'{price:.2f}',
        "quantity": quantity,
        "update_quantity": update_quantity,
    }

    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def cart_remove(request, product_id):
    '''
    REMOVE ITEM FROM CART
    '''
    cart = Cart(request)
    product_id = str(product_id)

    products = list(cart.cart.keys())

    if product_id in products:
        cart.remove(product_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def cart_detail(request):
    '''
    GET ALL ITEMS IN CART
    '''
    cart = Cart(request)

    items = []
    for key, value in cart.cart.items():
        products = Product.objects.filter(id=key).values(
            'id', 'name', 'price', 'quantity', 'category__name',
            'expire_date', 'has_expire_date', 'months_to_expire')

        for product in products:
            data = {
                'pk': product['id'],
                'name': product['name'],
                'price': product['price'],
                'quantity': product['quantity'],
                'variance': product['quantity'] - value['quantity'],
                'has_expire_date': product['has_expire_date'],
                'expire_date': product['expire_date'],
                'months_to_expire': product['months_to_expire'],
                
                'quantity_in_cart': value['quantity'],
                "total_price": value['total_price'],
            }
            items.append(data)

    if items:
        # return JsonResponse({"data":items},safe=False)
        return Response(items, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def cart_destroy(request):
    '''
        DESTROY ALL ITEMS  IN CART
    '''
    cart = Cart(request)
    # cart = cart.cart
    cart.clear()

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def cart_length(request):
    '''
    GET CART TOTAL AND PRICE TOTAL FOR ITEMS 
    '''
    cart = Cart(request)
    total_cart = len(cart)
    total_price = cart.get_total_price()

    cart = cart.cart
    print(cart)

    data = {
        'total_cart': total_cart,
        'total_price': total_price,
    }
    # print(len(cart), cart.get_total_price())

    return Response(data=data, status=status.HTTP_200_OK)
