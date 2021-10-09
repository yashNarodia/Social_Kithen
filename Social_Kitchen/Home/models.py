from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class TableReservation(models.Model):
    name =models.CharField(max_length=200)
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
