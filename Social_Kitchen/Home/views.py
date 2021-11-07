from django.contrib import auth
from django.shortcuts import redirect, render
from django.http import HttpResponse , HttpResponseRedirect
from .forms import SignupForm, UserCreationForm,TableReservationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import JsonResponse
import json
from .models import *


# Create your views here.
def HomePage(request):
    return render (request,'hometest.html')

def MenuPage(request):
    return render (request,'menu.html')

def ContactUsPage(request):
    return render (request,'contactus.html')

def AboutUsPage(request):
    return render (request,'aboutus.html')

def Cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
    else:
        items=[]
        order = {'get_Cart_total' :0 }
    context = {'items':items,'order':order}
    return render (request,'cart.html',context)

def Checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
    else:
        items=[]
        order = {'get_Cart_total' :0 }
    context = {'items':items,'order':order}
    return render(request, 'checkout.html' ,context)

def UpdateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    user = request.user
    customer, created = Customer.objects.get_or_create(user=user)
    print(customer)
    product = Dish.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer)

    orderItem, created = OrderItem.objects.get_or_create(order=order, dish=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def OrderNow(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order = {'get_Cart_total' :0 }
        cartItems = order['get_Cart_total']


    Dishes = Dish.objects.all()
    context = {'Dishes':Dishes , 'cartItems': cartItems }
    return render (request,'ordernow.html', context )


def SignUpPage(request):
    form = SignupForm(request.POST)

    if request.method == "POST":
        
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            firstName = form.cleaned_data.get('first_name')
            messages.success(request,'Account was Successfully Created for ' + firstName )
            return redirect('/login')
            
        
    context={ "form" : form }
    return render(request,"Signup.html",context)

def LoginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password)
        
        if user is not None:
            login(request,user) 
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is incorrect')

    context={}
    return render(request,"Login.html",context)

def LogoutUser(request):
    logout(request)
    return redirect('login') 


def TableReservation(request):
    form = TableReservationForm
    context = {'form':form}
    
    if request.method == 'POST':
        #  print(request.POST)
        form = TableReservationForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            messages.success(request,"Your table have been successfully reserved")
    
    return render(request,'table.html',context)

    #'TableReservation.html'