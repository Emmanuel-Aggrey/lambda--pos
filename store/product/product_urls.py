from accounts.accounts_decorators import change_default_password
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic.base import TemplateView

from store.product import product_views as views


app_name = 'product'
urlpatterns = [
    # path('category-home/', login_required(change_default_password(TemplateView.as_view(template_name='stores/category/categorys.html'))),name='category_home'),

    path('product-list/', views.product_views,name='products'),
    path('product-list/<int:pk>/', views.product_view,name='product'),

 



    
]


