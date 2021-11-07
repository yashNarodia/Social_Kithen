from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.base import Model

from django.db.models.deletion import CASCADE

# Create your models here.


class TableReservation(models.Model):
    name = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=10)
    partySize = models.IntegerField()
    time = models.TimeField()
    date = models.DateField()
    email = models.EmailField(max_length=200 ,null = True)

    def __str__(self):
        return str(self.name)

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.user)

class DishCategory(models.Model):
    categoryName = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.categoryName)


class Dish(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    price = models.DecimalField(max_digits=25, decimal_places=2,null=True,blank=True)
    description = models.TextField(max_length=400,null=True,blank=True)
    category =models.ForeignKey(DishCategory, on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField( null = True)

    def __str__ (self):
        return str(self.name)


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)+ " order of " + str(self.customer)

    @property
    def get_Cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True,blank=True)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True ,blank=True)

    def __str__(self):
        return str(self.order)

    @property
    def get_total(self):
        total = self.dish.price *self.quantity
        return total

class Customer_Address(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True,blank=True)
    Address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)

    def __str__(self):
        return str(self.Address)

# class Cart(models.Model):
#     customer = models.ForeignKey(User , on_delete=models.CASCADE)
#     subTotal = models.DecimalField(max_digits=25, decimal_places=2)
    

#     def __str__(self):
#         return str(self.customer)

# class CartItem(models.Model):
#     dish = models.ForeignKey(Dish,on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
#     quantity = models.IntegerField()
#     price = models.DecimalField(max_digits=25, decimal_places=2)

#     def __str__(self):
#         return str(self.dish)




