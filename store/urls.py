from accounts.accounts_decorators import change_default_password
from django.contrib.auth.decorators import login_required
from django.urls import path,include
from django.views.generic.base import TemplateView

from . import views

app_name = 'store'
urlpatterns = [
    path('unit-home/', include('store.units.units_urls')),
    path('generic-home/', include('store.generic.generic_urls')),
    path('category-home/', include('store.category.category_urls')),
    path('product-home/', include('store.product.product_urls')),

    # get the same categories in generic
    path('category-in-generics/<int:pk>/', views.categories_in_generics,name='categories_in_generics'),
    path('products-in-category/<int:pk>/', views.products_in_category,name='products_in_category'),


    path('issue/', login_required(change_default_password(TemplateView.as_view(template_name='stores/issue/store.html'))),name='issue'),

    # reqgular url to return all products in hierrachical order
    path('products/',views.all_products,name='all_products'),
    
]


