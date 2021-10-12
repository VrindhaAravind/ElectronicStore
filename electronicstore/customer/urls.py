from django.urls import path
from .views import RegistrationView,SignInView,HomePageView

urlpatterns=[
    path('register',RegistrationView.as_view(),name='register'),
    path('login',SignInView.as_view(),name='cust_signin'),
    path('home',HomePageView.as_view(),name='customer_home')

]
