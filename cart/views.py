from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.models import Product, Item
import requests
from django.http import JsonResponse
from cart.cart import Cart
from django.db.models import F


@api_view(['POST'])
def cart_add(request, cart_session_name='cart'):
    '''
    ADD ITEM TO CART
    '''
    cart = Cart(request, cart_session_name)

    data = request.data
    # cart_session_name = data.get('cart_session_name','cart') #get the cart session name
    product = data.get('id')
    price = '{:.2f}'.format(float(data['price']))
    price = eval(price)
    quantity = int(data['quantity'])
    update_quantity = eval(data.get('update_quantity', 'False').title())

    cart.add(product=product, price=price,
             quantity=quantity, update_quantity=update_quantity)

    # print("cart_session_name",cart_session_name)

    data = {
        "product": product,
        "price": f'{price:.2f}',
        "quantity": quantity,
        "update_quantity": update_quantity,
        "cart_session_name": cart_session_name,
    }

    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['DELETE', 'POST', 'GET'])
def cart_remove(request, product_id, cart_session_name='cart'):
    '''
    REMOVE ITEM FROM CART
    '''
    cart = Cart(request, cart_session_name)
    product_id = str(product_id)

    products = list(cart.cart.keys())
    # print(products)

    if product_id in products:
        cart.remove(product_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def cart_detail(request, cart_session_name='cart'):
    '''
    GET ALL ITEMS IN CART
    '''
    cart = Cart(request, cart_session_name)

    items = []
    for key, value in cart.cart.items():
        products = Product.objects.filter(id=key).values(
            'id', 'name', 'price', 'quantity', 'category__name',
            'expire_date', 'has_expire_date', 'months_to_expire')

        for product in products:
            data = {
                'pk': product['id'],
                'name': product['name'],
                'category__name': product['category__name'],
                'price': product['price'],
                'quantity': product['quantity'],
                'total': product['quantity'] + value['quantity'],
                'has_expire_date': product['has_expire_date'],
                'expire_date': product['expire_date'],
                'months_to_expire': product['months_to_expire'],

                'quantity_in_cart': value['quantity'],
                "total_price": value['total_price'],
                'cart_session_name': cart.value,
            }

            items.append(data)

    return Response(data=items, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def cart_destroy(request, cart_session_name='cart'):
    '''
        DESTROY ALL ITEMS  IN CART
    '''
    cart = Cart(request, cart_session_name)
    # cart = cart.cart
    cart.clear()

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def cart_length(request, cart_session_name='cart'):
    '''
    GET CART TOTAL AND PRICE TOTAL FOR ITEMS 
    '''
    cart = Cart(request, cart_session_name)
    total_cart = len(cart)
    total_price = cart.get_total_price()

    cart = cart.cart
    # print(cart)

    data = {
        'total_cart': total_cart,
        'total_price': total_price,
    }
    # print(len(cart), cart.get_total_price())

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST'])
def post_cart(request, cart_session_name='cart'):
    '''
        POST CART ITEMS TO DATABASE AND DESTROY THE CART
    '''
    cart = Cart(request, cart_session_name)

   
    for keys, values in cart.cart.items():

        items = Item.objects.bulk_create([
            Item(product_id=keys, quantity=values['quantity']
                 )])

        product = Product.objects.filter(pk=keys).update(
            quantity=F('quantity')+values['quantity'])

    cart.clear()

    return Response(data=product, status=status.HTTP_200_OK)
