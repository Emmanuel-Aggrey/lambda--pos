# from auditlog.registry import auditlog
from business.models import BaseModel, Supplier
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.shortcuts import reverse
from django.utils import timezone
from datetime import timedelta
from dateutil import relativedelta
from taggit.managers import TaggableManager


# Create your models here.

class Generic(BaseModel):
    name = models.CharField(
        help_text='eg paracetamol,beverage', max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def get_total_category(self):
        
        return self.generics.count()

    class  Meta:
        ordering = ['name','-date_created']


# auditlog.register(Generic)


class Unit(BaseModel):
    name = models.CharField(max_length=50,null=True, blank=True,help_text='Full name')
    unit = models.CharField(
        max_length=200, help_text='eg ml, mg, pcs', unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.unit)

    @property
    def get_total_products_by_unit(self):
        return self.units.count()

    def get_absolute_url(self):
        return reverse("unit-home/units", kwargs={"pk": self.pk})

    class Meta:
        ordering = ('-date_updated',)

# auditlog.register(Unit)


class Category(BaseModel):
    name = models.CharField(
        help_text='eg syrup,tablet,cream,shandy,guinness can 5 LT', max_length=100)
    # generic = models.ForeignKey(Generic, on_delete=models.CASCADE,
    #                             help_text='Paracetamol > syrup paracetamol > tablet', related_name='generics')
    description = models.TextField(null=True, blank=True)
    # unit = models.ForeignKey(Unit,on_delete=models.DO_NOTHING,null=True,related_name='units_of_measure')

    def __str__(self):
        return f'{self.name}:'

    @property
    def get_total_products(self):
        return self.categories.count()

    # @property
    # def generic_name(self):
    #     return self.generic.name

    @property
    def get_absolute_url(self):
        return reverse('store:category:category', args=[self.id])

        # store:generic:generic_home

        # /store/category-home/category-list/3/


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        # unique_together = [['name', 'generic']]
        ordering = ['name','-date_created']
        

    

# auditlog.register(Category)


class Product(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='categories', blank=True, null=True)
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE, blank=True, null=True, related_name='units')
    supplier = models.ManyToManyField(
        Supplier, blank=True, related_name='suppliers')
    receaved_date = models.DateField(
        blank=True, null=True, default=timezone.now)
    stock_level = models.PositiveIntegerField(
        default=10, blank=True, null=True)
    original_stock = models.PositiveIntegerField(
        default=0, null=True, blank=True, editable=False)
    shelf_number = models.CharField(max_length=20, blank=True, null=True)
    has_expire_date = models.BooleanField(default=False)
    months_to_expire = models.PositiveSmallIntegerField(default=0,blank=True)
    expire_date = models.DateField(blank=True, null=True)

    # tags = TaggableManager()

    class Meta:
        unique_together = [['name', 'unit']]
        index_together = ["name", "unit"]
        get_latest_by =['-receaved_date']

    @property
    def get_absolute_url(self):
        return reverse('store:products_in_category', args=[self.id])

    def __str__(self):
        # return f'{self.name} {self.category.name}'
        return self.name

    # def get_queryset(self, pks):
    #     return Product.objects.filter(pk__in=pks)
    @property
    def has_expired(self):

        if self.has_expire_date and self.expire_date:
            #
            difference = relativedelta.relativedelta(
                self.expire_date, timezone.now().date())
            print(difference)

            if timezone.now().date() >= self.expire_date or self.months_to_expire >= difference.months:
                return True
            else:
                return False
        else:
            return 'No Expire Date'
            
    @property
    def difference_btn_two_dates(date1, date2, *args):
        difference = relativedelta.relativedelta(date1, date2)
        return difference

    # @property
    # def category_name(self):
    #     return self.category.name

    # @property
    # def unit_name(self):
    #     return self.unit.unit

    # @property
    # def supplier_names(self):
    #     for names in self.supplier.all():
        
    #         return f'{names}'


@receiver(pre_save, sender=Product)
def update_original_stock(sender, instance, *args, **kwargs):
    if instance.quantity:

        instance.original_stock = int(
            instance.quantity) + int(instance.original_stock)
        # print('instance', instance.original_stock)
        # instance.save()


# auditlog.register(Product)

class Item(models.Model):
    name = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='items')
    serial_number = models.CharField(max_length=200, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('neworder:issue_in', args=[self.id, self.name.name])


# auditlog.register(Item)
