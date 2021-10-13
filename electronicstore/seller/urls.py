from django.urls import path
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home),
    path('login/',views.login),
    path('products/',views.products),
    path('register/', views.register, name='seller_registration'),
    path('products/edit/',views.products_edit),
    path('products/edit/confirm/',views.products_edit_confirm),
]
