from rest_framework import serializers
from .models import Product, Category, Generic


class GenericSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generic
        fields = ['name','description','id','get_total_category','date_created']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['pk','name', 'description',
                  'get_total_products','get_absolute_url']


    # def save(self):
    #     generic = self.validated_data['generic']

    #     print(generic)


class ProductSerializer(serializers.ModelSerializer):
    # supplier_names = serializers.ReadOnlyField(source='supplier.supplier')
    supplier = serializers.StringRelatedField(many=True,read_only=True)
    category_name = serializers.ReadOnlyField(source='category.name')
    unit_name = serializers.ReadOnlyField(source='unit.unit')
    generic_name = serializers.ReadOnlyField(source='category.generic.name')
    class Meta:
        model = Product
        fields = ['pk','name', 'price', 'quantity', 'description', 'generic_name','category','category_name',
                  'unit','unit_name', 'supplier','receaved_date', 'stock_level', 'original_stock',
                  'shelf_number', 'has_expire_date', 'months_to_expire',
                  'expire_date', 'has_expired','get_absolute_url']
