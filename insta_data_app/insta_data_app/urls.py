"""insta_data_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from data_app import views as data_app_views

urlpatterns = [
    path('', data_app_views.home, name ="home"),
    path('user/register/',data_app_views.register, name ="register_url" ),
    path('user/login/', data_app_views.login_view, name = "login"),
    path('user/logout/', data_app_views.logout_view, name = 'logout' ),
    path('admin/', admin.site.urls),
]
