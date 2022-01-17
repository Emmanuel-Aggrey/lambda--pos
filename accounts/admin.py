from django.contrib import admin

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','last_name','first_name','position','phone','is_staff','is_active','business',]
    list_editable =['position','phone','business','last_name','first_name','is_staff','is_active']
    list_display_links = ['username',]

admin.site.register(CustomUser, CustomUserAdmin)
 


