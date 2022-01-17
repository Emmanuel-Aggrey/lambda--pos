"""stores URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.views.generic.base import TemplateView
from accounts.accounts_decorators import change_default_password

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('business/',include('business.urls')),

    # path('api/', include('rest_framework.urls')),


    path('cart/', include('cart.urls')),
    # path('api/auth/', include('djoser.urls.authtoken')),


    path('store/',include('store.urls')),
    path('reports/',include('reports.urls')),
    path('', login_required(change_default_password(TemplateView.as_view(template_name='stores/index.html'))),name='home'),


    # path('charts/', change_default_password(TemplateView.as_view(template_name='charts.html')),name='charts'),

    path('charts/', login_required(change_default_password(TemplateView.as_view(template_name='stores/charts.html'))),name='charts'),



    path('employees/', login_required(change_default_password(TemplateView.as_view(template_name='accounts/employees.html'))),name='employees'),

    # path('employees/', change_default_password(TemplateView.as_view(template_name='accounts/employees.html')),name='employees'),

    # documentation
    path('docs/', include_docs_urls(title='LAMBDA API')),





    # path('',TemplateView.as_view(template_name='index.html',))

    path('session_security/', include('session_security.urls')),

  
]
