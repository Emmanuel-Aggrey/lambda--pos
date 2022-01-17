from django.contrib import admin
from .models import  Generic,Category,Unit,Product
# Register your models here.



# class CategoryInline(admin.TabularInline):
#     model = Category
  
#     list_display = ['generic','name','date_created','get_total_products']

  


# class GenericAdmin(admin.ModelAdmin):
#     list_display = ['name','date_created','get_total_category']
#     fields = ['name']
#     inlines = [CategoryInline]
#     search_fields = ('name',)

# admin.site.register(Generic, GenericAdmin)


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name','date_created','get_total_products']
#     # list_filter = ['generic']


@admin.register(Unit)
class UnitAdmtin(admin.ModelAdmin):
    list_display = ['name','unit','available','date_created','get_total_products_by_unit']
    list_editable = ['available']
    search_fields = ('name',)
  


# def has_expired(modeladmin,request,queryset):
#     queryset = queryset.filter(name='Dipex')
#     print(queryset)

 
# has_expired.short_description='Has Expired'


# @admin.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','quantity','category','unit','receaved_date','stock_level','has_expire_date','months_to_expire','expire_date','has_expired',]
    search_fields = ('name','category__name','unit__name')
    list_filter = ['category__name','unit']



class ProductInline(admin.TabularInline):
    model = Product
    list_display = ['name','quantity','category','unit','supplier','receaved_date','stock_level','has_expire_date','months_to_expire','expire_date','has_expired',]
    # actions = [has_expired]
    list_editable =['has_expire_date','months_to_expire','expire_date']
    list_filter =['category__name','unit__unit','supplier','months_to_expire',]
    # filter_horizontal = ['name','supplier']

  


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','description','date_created',]
    fields = ['name','description',]
    inlines = [ProductInline]
    
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)