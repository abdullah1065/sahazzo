from django.db import models

# Create your models here.


class DonatorTable(models.Model):
    D_ID = models.CharField(max_length=7)
    EMAIL = models.EmailField(max_length=50, primary_key=True)

class DonateTable(models.Model):
    D_ID = models.CharField(max_length=7)
    EVENT_ID = models.CharField(max_length=100)
    PAYMENT_DETAILS = models.CharField(max_length=30)
    PAYMENT = models.CharField(max_length=30)

class FundTable(models.Model):
    EVENT_ID = models.CharField(max_length=100, primary_key=True)
    COLLECTED_AMOUNT = models.IntegerField()
    FUND_STATUS = models.CharField(max_length=20)
    FUND_TAKEN_BY = models.CharField(max_length=100)
    

    