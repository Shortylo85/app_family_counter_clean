from django.contrib.auth.models import User
from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=256,null=True,blank=True)
    lat = models.DecimalField(max_digits=8,decimal_places=5,null=True,blank=True)
    lng = models.DecimalField(max_digits=8,decimal_places=5,null=True,blank=True)
    
class UserCity(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    city = models.ForeignKey(City, blank=True, null=True)
    
class Chat(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    message = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)