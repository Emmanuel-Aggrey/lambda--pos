from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from accounts.accounts_decorators import change_default_password
from .import views

app_name = 'business'
urlpatterns = [
    path('supliers/', login_required(change_default_password(TemplateView.as_view(template_name='business/supliers/supliers.html'))),name='supliers'),
    path('all-supliers/',views.suppliers,name='all_supliers'),
    path('create-supplier/',views.create_supplier,name='create_supplier'),
    path('update-supplier/<int:id>/',views.update_supplier,name='update-supplier'),

]