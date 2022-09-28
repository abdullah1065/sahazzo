from django.db import models

# Create your models here.
class PersonTable(models.Model):
    PersonType= models.CharField(max_length=7)
    FIRST_NAME = models.CharField(max_length=30)
    LAST_NAME = models.CharField(max_length=30)
    EMAIL = models.EmailField(max_length=50)
    CONTACT = models.CharField(max_length=20)
    NID = models.CharField(max_length=20)
    PASSWORD = models.CharField(max_length=50)
    CONFIRM_PASSWORD = models.CharField(max_length=50)

    def __str__(self):
        return 'self.id'
        
    