"""
URL configuration for realestate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path
from realestatedetails import views

urlpatterns = [
    path('',views.LoginForm,name='LoginForm'),
    path('Register/',views.Register,name='Register'),
    path('user_home/', views.User, name='user_home'),
    path('admin_home/', views.Admin, name='admin_home'),
    path('Client/', views.Client, name='Client'),
    path('Seller/',views.Seller,name='Seller'),
    path('PlotDetails/',views.PlotDetails,name='PlotDetails'),
    path('BI/',views.BI,name='BI'),
    path('Plotinfo/',views.Plotinfo,name='Plotinfo'),
    path('Viewed/',views.Viewed,name='Viewed'),
    path('client_details/',views.client_details,name='client_details'),
    path('seller_details/',views.seller_details,name='seller_details'),
    path('display_plotdetails/',views.display_plotdetails,name='display_plotdetails'),
    path('display_bi/',views.display_bi,name='display_bi'),
    path('display_plotinfo/',views.display_plotinfo,name='display_plotinfo'),
    path('display_viewed/',views.display_viewed,name='display_viewed'),
]
