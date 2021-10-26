from django.db import models
from django.contrib.auth.models import User
import datetime

from django.db.models.deletion import CASCADE

# Create your models here.


class TableReservation(models.Model):
    name = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=10)
    partySize = models.IntegerField()
    time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    rate = models.IntegerField(default=0)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(User, null=True, on_delete=models.CASCADE)



class OrderItem(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)



class DishCategory(models.Model):
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return str(self.categoryName)


class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    description = models.TextField(max_length=400)
    category =models.ForeignKey(DishCategory, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)



class Cart(models.Model):
    customer = models.ForeignKey(User , on_delete=models.CASCADE)
    subTotal = models.DecimalField(max_digits=25, decimal_places=2)
    

    def __str__(self):
        return str(self.customer)

class CartItem(models.Model):
    dish = models.ForeignKey(Dish,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=25, decimal_places=2)





