from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import User_registration_form
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from .models import Insta_profiles

# Create your views here.
@login_required
def home(request):
    if request.method == "POST":
        a = request.POST.getlist("filter_by")
        query = Insta_profiles.objects.all()
        print(request.POST['max_followers_value'])
        print(type(int(request.POST['max_followers_value'])))
        for i in a:
            if i == "Followers":
                query = Insta_profiles.objects.filter(follower_count__lte = int(request.POST['max_followers_value'])).filter(follower_count__gte = int(request.POST['min_followers_value']))
                print(len(query))
            elif i == "Followees":
                query = query.filter(following_count__lte = int(request.POST['max_followees_value'])).filter( following_count__gte = int(request.POST['min_followees_value']))

        number = len(query)
        return render(request, "filter_results.html", {"page":query, "number":number})

    else:
        profiles = Insta_profiles.objects.all()
        p = Paginator(profiles, 10)
        page_num = request.GET.get('page',1)
       
        try:
            page = p.page(page_num)

        except EmptyPage:
            page = p.page(1)

    return render(request, 'home.html', {"page":page})


def register(request):
    if request.user.is_authenticated:
        messages.warning(request, "Please Logout to create a new account!")
        return redirect('home')
    form  = User_registration_form()
    if request.method == "POST":
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully! Please Login to continue..")
            return redirect('login')
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