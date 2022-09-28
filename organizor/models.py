from django.db import models
from home.models import PersonTable
# Create your models here.

class OrganizorTable(models.Model):
    O_ID = models.CharField(max_length=7)
    EMAIL = models.EmailField(max_length=50, primary_key=True)

class EventTable(models.Model):
    EVENT_NAME = models.CharField(max_length=80)
    START_TIME = models.DateField()
    END_TIME = models.DateField()
    LOCATION = models.CharField(max_length=40)
    BUDGET = models.IntegerField()
    SHOP = models.CharField(max_length=50)
    ITEMS = models.CharField(max_length=40)
    QUANTITY = models.IntegerField()
    EVENT_FOR = models.CharField(max_length=80)
    CREATED_BY = models.CharField(max_length=100)
    
    
class ShopTable(models.Model):
    SHOP_NAME = models.CharField(max_length=80)
    PAY_DEMAND = models.CharField(max_length=20)
    DELIVERY_STATUS = models.CharField(max_length=50)
    