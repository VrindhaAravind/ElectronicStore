from django.shortcuts import render
from django.views.generic import ListView
from customer.models import Orders
# Create your views here.

def OrderList(request):
    
    all_orders=Orders.objects.all()


    return render(request,'all_orders.html',{'all_orders':all_orders})