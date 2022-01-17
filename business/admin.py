from django.contrib import admin
from .models import Business,Supplier
from accounts.models import CustomUser
from store.models import Product
from accounts.forms import CustomUserCreationForm,CustomUserChangeForm
# Register your models here.


# admin.site.register(Business)


# class CustomUserInline(admin.TabularInline):
#     model = CustomUser
#     # add_form = CustomUserCreationForm
#     # form = CustomUserChangeForm
#     fields = ['username','first_name','last_name','position','phone','email',]

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone','location','head','available','date_created','get_users_total',]
    list_filter = ['name','available']
    # inlines = [CustomUserInline]
    search_fields = ('phone','name','location','head',)
    list_editable = ['available',]
    list_display_links = ['name','phone',]

# admin.site.register(Business, BusinessAdmin)



# class ProductInline(admin.TabularInline):
#     model = Product
#     # add_form = CustomUserCreationForm
#     # form = CustomUserChangeForm
#     fields = ['name','quantity','unit','supplier','has_expire_date','expire_date',]



class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone','location','available','date_created','get_total_purchased']
    list_filter = ['name','available']
    # inlines = [ProductInline]
 
    search_fields = ('phone','name','location')
    list_editable = ['available',]
    list_display_links = ['name','phone',]

admin.site.register(Supplier, SupplierAdmin)


