from django.urls import path
from .views import RegistrationView,SignInView,HomePageView,ViewProduct,add_to_cart,MyCart,DeleteFromCart,WriteReview,place_order,view_orders,cancel_order,add_address,view_address,edit_address,delete_address
from . import views
urlpatterns=[
    path('register',RegistrationView.as_view(),name='register'),
    path('login',SignInView.as_view(),name='cust_signin'),
    path('signout',views.signout,name='signout'),
    path('home',HomePageView.as_view(),name='customer_home'),
    path('search',views.search,name="search"),
    path('mobiles',views.mobiles,name="mobiles"),
    path('laptops',views.laptops,name="laptops"),
    path('tablets',views.tablets,name="tablets"),
    path('price_low_to_high',views.price_low_to_high,name="price_low_to_high"),
    path('price_high_to_low', views.price_high_to_low, name="price_high_to_low"),
    path('apple', views.apple, name="apple"),
    path('lenovo', views.lenovo, name="lenovo"),
    path('oppo', views.oppo, name="oppo"),
    path('oneplus', views.oneplus, name="oneplus"),
    path('redmi', views.redmi, name="redmi"),
    path('samsung', views.samsung, name="samsung"),
    path("view_profile",views.ViewDetails, name="view_profile"),
    path("edit", views.EditDetails.as_view(), name="edit_profile"),
    path('viewproduct/<int:id>',ViewProduct.as_view(),name='viewproduct'),
    path('addtocart/<int:pk>',add_to_cart,name='addtocart'),
    path('mycart',MyCart.as_view(),name='mycart'),
    path('removeitem/<int:pk>',DeleteFromCart.as_view(),name='deletecart'),
    path('review/<int:pk>',WriteReview.as_view(),name='review'),
    path("placeorder/<int:id>/<int:cid>", place_order, name="placeorder"),
    path("vieworders", view_orders, name="vieworders"),
    path("removeorder/<int:id>", cancel_order, name="removeorder"),
    path('add_address',add_address,name='add_address'),
    path('view_address',view_address,name='view_address'),
    path('address/change/<int:id>',edit_address,name='edit_address'),
    path('address/delete/<int:id>',delete_address,name='delete_address'),
    path('viewproduct/<int:id>/writereview',views.WriteReview.as_view(),name='write_review'),



]