from django.contrib.auth.models import User
from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=64,null=True,blank=True)
    country = models.CharField(max_length=64,null=True,blank=True)
    lat = models.DecimalField(max_digits=7,decimal_places=4)
    lng = models.DecimalField(max_digits=7,decimal_places=4)
    
class UserCity(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    city = models.ForeignKey(City, blank=True, null=True)