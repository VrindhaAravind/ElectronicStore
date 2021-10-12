from django.db import models
from django.contrib.auth.models import User

# Create your models here.
Role_Choices=(
    ('admin','ADMIN'),
    ('seller','Seller'),
    ('customer','Customer')
)

class Seller_Details(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    account_number = models.IntegerField()
    ifsc_code = models.CharField(max_length=20)

class User_Role(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=10,choices=Role_Choices,default='customer')


class Products(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    offer = models.FloatField()

    def __str__(self):

        return self.product_name