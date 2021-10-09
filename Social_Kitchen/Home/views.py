from django.contrib import auth
from django.shortcuts import redirect, render
from django.http import HttpResponse , HttpResponseRedirect
from .forms import SignupForm, UserCreationForm,TableReservationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def HomePage(request):
    return render (request,'home.html')

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
    
    return render(request,'TableReservation.html',context)