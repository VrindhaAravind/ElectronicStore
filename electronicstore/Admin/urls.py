from django.urls import path
from .views import OrderList

urlpatterns = [
        path('allorders',OrderList,name='all_order_list')
]