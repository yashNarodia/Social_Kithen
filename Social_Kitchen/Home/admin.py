from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class TableAdmin(admin.ModelAdmin):
    list_display= ('name','partySize','time', 'date','phoneNumber')
    

admin.site.register(TableReservation, TableAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display= ('customer','subTotal')
    
admin.site.register(Cart , CartAdmin)
admin.site.register(CartItem)
admin.site.register(Dish)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(DishCategory)






