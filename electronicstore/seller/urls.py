from django.urls import path
from django.shortcuts import render,redirect
from .views import register


urlpatterns = [
            path('register',register,name='seller_registration'),
            path('base',lambda request : render(request,'seller_base.html'),name='base')
    
]

