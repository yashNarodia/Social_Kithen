from django import forms
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.forms import Form
from django.forms.models import ModelForm
from .models import *

class SignupForm(UserCreationForm):
    MobileNo = forms.CharField(max_length=10)
    #Name = forms.CharField()

    class Meta: 
        model = User
        #fields = ['Name','username','MobileNo','email','password1','password2']
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email','MobileNo')

class TableReservationForm(ModelForm):
    
    class Meta:
        model = TableReservation
        fields = '__all__'


