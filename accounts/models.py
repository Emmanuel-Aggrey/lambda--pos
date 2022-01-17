# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from business.models import BaseModel, Business
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect, reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group
class CustomUser(AbstractUser,BaseModel):
    # add additional fields in here
    #attach business to user
    business = models.ForeignKey(Business,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='business_names') 
    # position =models.CharField(max_length=200,null=True, blank=True)
    position =models.ForeignKey(Group,on_delete=models.DO_NOTHING,null=True)

    phone = models.CharField(max_length=15,help_text='optional',unique=True,null=True, blank=True)
    # available = models.BooleanField(default=True)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
    @property
    def get_full_name(self):
        if self.first_name or self.last_name:
            return self.first_name + " " + self.last_name
        if self.username:
            return self.username
        else:
            return 'Not Loged in'
    @property
    def get_users_by_business_name(self):
        return reverse("employees", kwargs={"business_slug": self.business.slug})
    # get_users_by_business_name

    @property
    def has_no_business(self):
        if not self.business:
            return reverse('login')
        

        

@receiver(post_save, sender=CustomUser)
def post_save_handler(sender, instance, created, *args, **kwargs):
    if instance.username:
        print(instance)
        # print(instance.username.set_password(instance.password))
        # instance.user
        # slug = slugify(instance.name)
        # instance.slug = slug+'-'+str(instance.id)
        # instance.save()




# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
