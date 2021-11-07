from django.urls import path
from django.urls.conf import include
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

#    Admin Header Customizaiton

admin.site.site_header = "Social Kitchen Admin Access"
admin.site.site_title = "Social Kitchen dashboard"
admin.site.index_title = "Welcome to Dasborad"

urlpatterns = [
    path('',views.HomePage, name='home'),
    path('signup/',views.SignUpPage, name='SignUp'),
    path('login/',views.LoginPage, name='login'),
    path('logout/',views.LogoutUser, name='logout'),
    path('TableReservation/',views.TableReservation,name='TableReservation'),
    path('Menu/',views.MenuPage,name='Menu'),
    path ('ContactUs',views.ContactUsPage,name='ContactUs'),
    path('AboutUs',views.AboutUsPage, name='AboutUs'),
    path('OrderNow',views.OrderNow,name = 'OrderNow'),
    path('Cart',views.Cart,name='Cart'),
    path('Checkout',views.Checkout,name='Checkout'),
    path('Update_item/',views.UpdateItem,name='UpdateItem')
    
    ]  

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)