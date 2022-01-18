from accounts.accounts_decorators import change_default_password
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic.base import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

from store.category import category_views as views

app_name = 'category'
urlpatterns = [
    # path('category-home/', login_required(change_default_password(TemplateView.as_view(template_name='stores/category/categorys.html'))),name='category_home'),

    path('category-list/', views.category_views,name='categories'),
    path('category-list/<int:pk>/', views.category_view,name='category'),

]


