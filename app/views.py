from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Customer
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def index(request):
    return render(request,"index.html")
def blog(request):
    return render(request,"blog.html")
def package(request):
    return render(request,"package.html")
def testimonial(request):
    return render(request,"testimonial.html")
def signup(request):
    if request.method == 'POST':
        user = Customer()
        user.name = request.POST['name']
        user.contact = request.POST['contact']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.repassword = request.POST['repassword']
        if user.password != user.repassword:
            return redirect('signup')
        else:
            user.save()
    return render(request,"signup.html")
def loginpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email = email, password = password)

        if user is not None:
            login(request, user)
            return redirect(request,'about')
        else:
            return redirect('testimonial')

    return render(request,'login.html')

    #else:
        #data = Customer.objects.all()
        #return render(request,"login.html",{"data": data})
def about(request):
    return render(request,"about.html")
def booking(request):
    return render(request,"booking.html")
def navbar(request):
    return render (request,"navbar.html")
