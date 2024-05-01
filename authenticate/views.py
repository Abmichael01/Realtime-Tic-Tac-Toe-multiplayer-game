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
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        username = request.POST.get('username')

        if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken")
                return redirect("register")
        
        if form.is_valid():
            form.save()
            messages.success(request, "You account has been created successfully")
        else:
            if '__all__' in form.errors:
                error_message = form.errors['__all__'][0].message
            else:
                error_message = "Form is invalid"
            messages.error(request, error_message)
            
            
    return render(request, "authenticate/login-register.html", {
        "page": "register",
        
    })

def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("login")