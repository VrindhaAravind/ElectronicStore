
from django.db import models
from seller.models import Products
from django.contrib.auth.models import User

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

class Orders(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.CharField(max_length=120)
    address=models.TextField()
    seller = models.CharField(max_length=250,default=None)
    options=(
        ("ordered","ordered"),
        ("packed","packed"),
        ("shipped","shipped"),
        ("delivered","delivered"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=120,choices=options,default="ordered")
    date=models.DateField(auto_now=True)


class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    review=models.CharField(max_length=500)
    date=models.DateField(auto_now=True)



class Address(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=50)
    address_line = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255)
    town_city = models.CharField(max_length=150)
    delivery_instructions = models.CharField(max_length=255)

    def __str__(self):
        return self.name+","+self.address_line+','+self.address_line2+','+self.phone+','+self.town_city+','+self.pin_code
