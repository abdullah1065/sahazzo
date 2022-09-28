from django.db import models

# Create your models here.

class VolunteerTable(models.Model):
    V_ID = models.CharField(max_length=7)
    EMAIL = models.EmailField(max_length=50, primary_key=True)
    STATUS = models.CharField(max_length=20)
    VOLUNTARY = models.CharField(max_length=100)
