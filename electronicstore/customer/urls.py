from django.urls import path
<<<<<<< HEAD
from customer.views import RegistrationView,SignInView,HomePageView

urlpatterns=[
    path('register',RegistrationView.as_view(),name='register'),
    path('login',SignInView.as_view(),name='cust_signin'),
    path('home',HomePageView.as_view(),name='customer_home')

]
=======

urlpatterns = [

]
>>>>>>> 1b5d59eb531923428a3327cace5c5c696dd49e79
