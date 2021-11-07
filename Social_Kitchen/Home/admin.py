from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class TableAdmin(admin.ModelAdmin):
    list_display= ('name','partySize','time', 'date','phoneNumber')

admin.site.register(TableReservation, TableAdmin)

admin.site.register(Customer)

class DishAdmin(admin.ModelAdmin):
    list_display = ('name','category','price')

admin.site.register(Dish,DishAdmin)
admin.site.register(DishCategory)

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','customer']

admin.site.register(Order,OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display=['order','dish','quantity']
admin.site.register(OrderItem,OrderItemAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display=['customer','Address']

admin.site.register(Customer_Address,AddressAdmin)





