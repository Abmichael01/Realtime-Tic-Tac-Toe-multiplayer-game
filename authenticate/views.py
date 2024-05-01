from django.shortcuts import render, redirect
from . forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # if User.objects.filter(username=username).exists():
        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            return redirect("lobby")
        else:
            messages.error(request, "Email or pasword is incorrect")

    return render(request, "authenticate/login-register.html", {
        "page": "login",
    })

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken")
                return redirect("register")
        
        if password1!= password2:
            messages.error(request, "Passwords do not match")
            return redirect("register")
        
        user = User.objects.create_user(username=username)
        user.set_password(password1)
        user.save()
        
        messages.success(request, "Successful, You can now login")
        return redirect("login")
        
            
            
    return render(request, "authenticate/login-register.html", {
        "page": "register",
        
    })

def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("login")