from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from .forms import RegistrationForm, LoginForm,UpdateForm
from .models import Cart
from seller.models import Products
from .decorators import signin_required
from django.utils.decorators import method_decorator

#Registration and signin

class RegistrationView(TemplateView):
    form_class = RegistrationForm
    template_name = "registration.html"
    model = User
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cust_signin")


class SignInView(TemplateView):
    template_name = "login.html"
    form_class = LoginForm
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("customer_home")
            else:
                self.context["form"] = form
                return render(request, self.template_name, self.context)

@method_decorator(signin_required,name="dispatch")
class HomePageView(TemplateView):
    template_name = 'homepage.html'
    model = Products
    context_object_name = "products"

@signin_required
def signout(request):
    logout(request)
    return redirect("signin")

@signin_required
def update_details(request):
    # detail=Userdetails.objects.get()
    form = UpdateForm()
    if request.method == "GET":
        context = {"form": form}
        return render(request, "user_details.html", context)
    elif request.method == "POST":
        form = UpdateForm(request.POST, request.FILES)
        if form.is_valid() :
            form.save()
            return redirect("customer_home")
        else:
            context = {"form": form}
            return render(request, "user_details.html", context)
        
       
class ViewProduct(TemplateView):
    template_name = 'productdetail.html'
    context={}
    def get(self, request, *args, **kwargs):
        id=kwargs['pk']
        product=Products.objects.get(id=id)
        reviews=Review.objects.filter(product=product)
        self.context['product']=product
        self.context['reviews']=reviews
        return render(request,self.template_name,self.context)

def add_to_cart(request,*args,**kwargs):
    id=kwargs['pk']
    product=Products.objects.get(id=id)
    cart=Cart(product=product,user=request.user)
    cart.save()
    return redirect('mycart')

class MyCart(TemplateView):
    template_name = 'cart.html'
    context={}
    def get(self, request, *args, **kwargs):
        cart_products=Cart.objects.filter(user=request.user,status='ordernotplaced')
        self.context['cart_products']=cart_products
        return render(request,self.template_name,self.context)

class DeleteFromCart(TemplateView):
    def get(self, request, *args, **kwargs):
        id=kwargs['pk']
        cart_product=Cart.objects.get(id=id)
        cart_product.delete()
        return redirect('mycart')

class WriteReview(TemplateView):
    template_name = 'review.html'
    context={}
    def get(self, request, *args, **kwargs):
        form=ReviewForm()
        self.context['form']=form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        id=kwargs['pk']
        product=Products.objects.get(id=id)
        form=ReviewForm(request.POST)
        if form.is_valid():
            review=form.cleaned_data.get('review')
            new_review=Review(user=request.user,product=product,review=review)
            new_review.save()
            return redirect('viewproduct',product.id)
