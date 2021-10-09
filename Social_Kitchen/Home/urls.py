from django.urls import path
from django.urls.conf import include
from . import views
from django.contrib import admin
#    Admin Header Customizaiton

admin.site.site_header = "Social Kitchen Admin Access"
admin.site.site_title = "Social Kitchen dashboard"
admin.site.index_title = "Welcome to Dasborad"

urlpatterns = [
    path('',views.HomePage, name='home'),
    path('signup/',views.SignUpPage, name='SignUp'),
    path('login/',views.LoginPage, name='login'),
    path('logout/',views.LogoutUser, name='logout'),
    path('TableReservation/',views.TableReservation,name='TableReservation')
    

    ]  