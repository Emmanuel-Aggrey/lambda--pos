from accounts.accounts_decorators import change_default_password
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic.base import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

from store.generic import generic_views as views

app_name = 'generic'
urlpatterns = [
    path('generic-home/', login_required(change_default_password(TemplateView.as_view(template_name='stores/category/categorys.html'))),name='generic_home'),

    # GET GENERICS 
    path('generic-list/',views.generic_views,name='generic_list'),

    #PUT, GET GENERIC
    path('generic-list/<int:pk>/', views.generic_view,name='generic'),



    
]


