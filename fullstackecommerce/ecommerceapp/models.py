from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Carousel(models.Model):
    image1 = models.ImageField(upload_to="uploads/images")
    image2 = models.ImageField(upload_to="uploads/images")
    image3 = models.ImageField(upload_to="uploads/images")

class Brand(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="uploads/brands") 

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200,default="")
    description = models.TextField(max_length=2000,default="")
    price = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    minimumquantity = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Register(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.PositiveIntegerField(default=+91)
    pincode = models.PositiveIntegerField(default=0)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user.first_name

class Ad(models.Model):
    image = models.ImageField(upload_to="uploads/ads")


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    message = models.TextField(max_length=300)

    def __str__(self):
        return self.name


