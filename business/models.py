from django.db import models
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.utils.text import slugify


# Create your models here.

# abstract models
class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

# abstract models
class Organization(BaseModel):
    name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True,editable=False,blank=True,null=True)
    phone = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    available = models.BooleanField(default=True)
  

    class Meta:
        abstract = True

class Business(Organization):  
    head = models.CharField(max_length=200)
    def __str__(self):
        return '{}: By {} '.format(self.name, self.head)


    class Meta:
        verbose_name ='Business'
        verbose_name_plural = 'Businesses'

    @property
    def get_users_total(self):
        return self.business_names.count()

# create slug from Business name
@receiver(pre_save, sender=Business)
def post_save_business_handler(sender, instance, *args, **kwargs):
    if instance:
        slug = slugify(instance.name)
        instance.slug = slug
        # instance.save()



class Supplier(Organization):

    def __str__(self):
        # suppliers ={'pk':self.pk, 'name':self.name}
        # suppliers ={'name':self.name}

        return  self.name #f'{suppliers}'
    
    @property
    def get_total_purchased(self):
        return self.suppliers.count()



# create slug from Supplier name
@receiver(pre_save, sender=Supplier)
def post_save_supplier_handler(sender, instance, *args, **kwargs):
    if instance:
        slug = slugify(instance.name)
        instance.slug = slug
        # instance.save()

