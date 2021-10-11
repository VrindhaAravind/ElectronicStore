from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Seller_Details(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField()
    bank_name = models.CharField(max_length=100)
    account_number = models.IntegerField()
    ifsc_code = models.CharField(max_length=20)


