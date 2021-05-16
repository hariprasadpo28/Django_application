from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import User_registration_form
from django.contrib import messages

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.user.is_authenticated:
        messages.warning(request, "Please Logout to create a new account!")
        return redirect('home')
    form  = User_registration_form()
    if request.method == "POST":
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            #errors = form.errors
            form = User_registration_form(request.POST)
            return render(request, 'register.html', {"registerform":form})
            
    return render(request, 'register.html', {"registerform":form})


 
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect('home')
        else:
            form = AuthenticationForm(request.POST)
            messages.warning(request, "Invalid Credentials")
            return render(request,'login.html',{'login_form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'login_form':form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        messages.warning(request, "You are not logged in!")
    return redirect('login')