from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class TableAdmin(admin.ModelAdmin):
    list_display= ('name','partySize','time', 'date','phoneNumber')
    

admin.site.register(TableReservation, TableAdmin)

