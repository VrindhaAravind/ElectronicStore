from django.urls import path
from .views import RegistrationView,SignInView,HomePageView,update_details,ViewProduct,add_to_cart,MyCart,DeleteFromCart
urlpatterns=[
    path('register',RegistrationView.as_view(),name='register'),
    path('login',SignInView.as_view(),name='cust_signin'),
    path('home',HomePageView.as_view(),name='customer_home'),
    path("update",update_details,name="update"),
    path('viewproduct/<int:pk>',ViewProduct.as_view(),name='viewproduct'),
    path('addtocart/<int:pk>',add_to_cart,name='addtocart'),
    path('mycart',MyCart.as_view(),name='mycart'),
    path('removeitem/<int:pk>',DeleteFromCart.as_view(),name='deletecart')


]
