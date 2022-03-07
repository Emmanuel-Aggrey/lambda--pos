from django.urls import  path
from . import views

app_name = 'cart'

urlpatterns = [
    path('<str:cart_session_name>/', views.cart_detail, name='cart_detail'),
    path('add/<str:cart_session_name>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/<str:cart_session_name>/', views.cart_remove, name='cart_remove'),
    path('destroy/<str:cart_session_name>/', views.cart_destroy, name='cart_destroy'),
    path('cart_length/<str:cart_session_name>/', views.cart_length, name='cart_length'),
    path('post_cart/<str:cart_session_name>/', views.post_cart, name='post_cart'),


]

