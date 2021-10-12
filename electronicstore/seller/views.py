from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.models import User, auth
from django.http import HttpResponse

# Create your views here.

def login(request):
    if request.method=='POST':
        # print(request.POST.get('username'),request.POST.get('password'))
        id=User.objects.get(username=request.POST.get('username')).pk
        # print(id)
        if models.Seller_Details.objects.filter(username =request.POST.get('username')).exists():
            print('user exist')
            print(models.Seller_Details.objects.get(username ='manu').user)
            user=auth.authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                return render(request,'seller_login.html')
    return render(request,'seller_login.html')

def home(request):
    return HttpResponse('Welcome Home')