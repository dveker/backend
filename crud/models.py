from email.policy import default
from itertools import product
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Product(models.Model):
    carss = [
    ('SUV'),
    ('Sedan'),
    ('cupe'),
    ('pickup'),
    ('small'),
    ]
    name = models.CharField(max_length=200)
    modelcar = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    digital = models.BooleanField(default=False,null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url