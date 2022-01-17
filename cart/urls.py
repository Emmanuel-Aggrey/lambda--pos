from django.urls import  path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('destroy/', views.cart_destroy, name='cart_destroy'),
    path('cart_length/', views.cart_length, name='cart_length'),


]

