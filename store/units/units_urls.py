from accounts.accounts_decorators import change_default_password
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic.base import TemplateView

from store.units import units_view as views

app_name = 'unit'
urlpatterns = [
    path('unit-home/', login_required(change_default_password(TemplateView.as_view(template_name='stores/units/units_of_mesurements.html'))),name='unit_home'),

    path('units/', views.units,name='units'),
    path('units/<int:id>/', views.units,name='units'),
    
]


