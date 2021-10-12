from django.db import models
from seller.models import Products

class Userdetails(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=15,blank=False)
    dob = models.DateField(blank=True,null=True)
    image = models.ImageField(upload_to="images",blank=True)

    def __str__(self):
        return self.first_name

class Cart(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.CharField(max_length=120)
    options=(("ordernotplaced","ordernotplaced"),
             ("orderplaced","orderplaced")
             )
    status=models.CharField(max_length=120,choices=options,default="ordernotplaced")
