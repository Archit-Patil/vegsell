from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import models

# Create your views here.
def register(request):
    if request.method=="POST":
        username = request.POST['username']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password != confirmpassword:
            messages.error(request, "Passwords do not match")
            redirect('vegetables-register')
        
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = firstName
            myuser.last_name = lastName
            myuser.save()
            messages.success(request, 'Your account has been successfully created')
            redirect('vegetables-login')

    return render(request, 'User/register.html')

def userlogin(request):
    if request.method=="POST":
            loginusername = request.POST['loginusername']
            loginpassword = request.POST['loginpassword']
            user = authenticate(username=loginusername, password=loginpassword)

            if user is not None:
                login(request,user)
                messages.success(request, "Successfully logged in")
                return redirect('vegetables-home')
            else:
                messages.error(request, "Invalid Credientials")
                return redirect('vegetables-login')
        

    return render(request, 'User/login.html')

def userlogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('vegetables-home')