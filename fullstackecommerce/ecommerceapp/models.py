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
    image = models.ImageField(upload_to="uploads/categories",default="")

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200,default="")
    description = models.TextField(max_length=3500,default="")
    price = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/productimages",default="") 
    minimumquantity = models.CharField(max_length=100)
    discount = models.PositiveIntegerField(default=0,null=True,blank=True)
    is_available = models.BooleanField(default=True)

    @staticmethod
    def product_by_categories(category_id):
        if category_id:
            return Product.objects.filter(category=category_id,is_available=True)
        else:
            return Product.objects.filter(is_available=True)    


    def __str__(self):
        return self.name

class Register(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,default="")
    mobile  = models.IntegerField(default=0)
    address = models.TextField(max_length=2000)
    city = models.CharField(max_length=300)
    pincode = models.IntegerField(default="")
    state = models.CharField(max_length=100,default="")

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
        

class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)

    statuses = [
        ('success','success'),
        ('fail','fail')
    ]        
    status = models.CharField(choices=statuses,max_length=200)
    orderid = models.CharField(max_length=300,default="")
    paymentid = models.CharField(max_length=300,default="")

    def __str__(self):
        return self.user.first_name

class Userproduct(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,default="")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    orderid = models.CharField(max_length=200,default="")
    paymentid = models.CharField(max_length=200,default="")
    totalprice = models.FloatField(default=0)
    delstatus = [
        ('Accepted','Accepted'),
        ('Packed','Packed'),
        ('Shipped','Shipped'),
        ('on the way','on the way'),
        ('delievered','delievered')
    ]

    status = models.CharField(choices=delstatus,max_length=300,default="Accepted")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name