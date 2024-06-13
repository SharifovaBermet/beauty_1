from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, login, logout

def home_page(request):
    services = Services.objects.all()
    services_view = Service_View.objects.all()
    return render(request,'index.html', {'services': services, 'view': services_view})

def pricing(request):
    services = Services.objects.all()
    services_view = Service_View.objects.all()
    return render(request,'pricing.html', {'services': services, 'view': services_view})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def specialist(request):
    masters = Master.objects.all()
    # print(master)
    return render(request,'specialists.html', {"masters_info":masters})

def blog(request):
    return render(request,'blog.html')

def login_info(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(username=email)
  
        login(request, user)
        return redirect('home') 
    return render(request,'login.html')

def logout_info(request):
    logout(request)
    return redirect('home') 
    

def registrations(request):
    if request.method == 'POST':
        name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(first_name=name, username=email, email=email, password=password)
        user = authenticate(username=email,password=password)
        if user is not None:
                login(request, user)
                return redirect('home') 
    return render(request,'registrations.html')



def services_test(request):
    pass # - забронить, обознить пустую функцию
# def - обозначение функции