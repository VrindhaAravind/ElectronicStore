from django.shortcuts import render, redirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from .forms import RegistrationForm,LoginForm,UpdateForm,ReviewForm,PlaceOrderForm,UserAddressForm
from .models import Cart,Review,Orders,Address
from seller.models import Products
from .decorators import signin_required
from django.utils.decorators import method_decorator


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


@method_decorator(signin_required, name="dispatch")
class HomePageView(TemplateView):
    template_name = 'homepage.html'
    context={}
    def get(self, request, *args, **kwargs):
        products = Products.objects.all()
        self.context['products']=products
        return render(request, self.template_name,self.context)

@signin_required
def signout(request):
    logout(request)
    return redirect("cust_signin")


@signin_required
def update_details(request):
    # detail=Userdetails.objects.get()
    form = UpdateForm()
    if request.method == "GET":
        context = {"form": form}
        return render(request, "user_details.html", context)
    elif request.method == "POST":
        form = UpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("customer_home")
        else:
            context = {"form": form}
            return render(request, "user_details.html", context)


class ViewProduct(TemplateView):
    template_name = 'productdetail.html'
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        product = Products.objects.get(id=id)
        reviews = Review.objects.filter(product=product)
        self.context['product'] = product
        self.context['reviews'] = reviews
        return render(request, self.template_name, self.context)


def add_to_cart(request, *args, **kwargs):
    id = kwargs['pk']
    product = Products.objects.get(id=id)
    cart = Cart(product=product, user=request.user)
    cart.save()
    return redirect('mycart')


class MyCart(TemplateView):
    template_name = 'cart.html'
    context = {}

    def get(self, request, *args, **kwargs):
        cart_products = Cart.objects.filter(user=request.user, status='ordernotplaced')
        self.context['cart_products'] = cart_products
        return render(request, self.template_name, self.context)


class DeleteFromCart(TemplateView):
    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        cart_product = Cart.objects.get(id=id)
        cart_product.delete()
        return redirect('mycart')


class WriteReview(TemplateView):
    template_name = 'review.html'
    context = {}

    def get(self, request, *args, **kwargs):
        form = ReviewForm()
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs['pk']
        product = Products.objects.get(id=id)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.cleaned_data.get('review')
            new_review = Review(user=request.user, product=product, review=review)
            new_review.save()
            return redirect('viewproduct', product.id)

def place_order(request,*args,**kwargs):
    id=kwargs.get("id")
    product=Products.objects.get(id=id)
    instance={
        "product":product.product_name
    }
    form=PlaceOrderForm(initial=instance)


    context={}
    context["form"]=form


    if request.method=="POST":
        cid=kwargs.get("cid")

        cart=Cart.objects.get(id=cid)
        
        form=PlaceOrderForm(request.POST,request.user)
        if form.is_valid():
            address=form.cleaned_data.get("address")
            product=product
            order=Orders(address=address,product=product,user=request.user,seller=product.user.username)
            print(product.user.username)
            order.save()
            
            cart.status="orderplaced"
            cart.save()

            return redirect("customer_home")

    return render(request,"placeorder.html",context)

def view_orders(request,*args,**kwargs):
    orders=Orders.objects.filter(user=request.user)

    context={
        "orders":orders,
    }
    return render(request,"vieworders.html",context)

def cancel_order(request,*args,**kwargs):
    id=kwargs.get("id")
    order=Orders.objects.get(id=id)
    order.status="cancelled"
    order.save()
    return redirect("vieworders")



def add_address(request):

    if request.method == 'POST':
        address_form = UserAddressForm(data=request.POST)
        if address_form.is_valid():
            address_form = address_form.save(commit=False)
            address_form.user = request.user
            address_form.save()
            return redirect('mycart')
    else:
        address_form = UserAddressForm()
    return render(request,'add_address.html',{'form':address_form})

def view_address(request):

    addresses = Address.objects.filter(user=request.user)
    return render(request,'view_address.html',{'addresses':addresses})

def edit_address(request,id):

    if request.method == "POST":
        address = Address.objects.get(pk=id,user=request.user)
        address_form = UserAddressForm(instance=address,data=request.POST)
        if address_form.is_valid():
            address_form.save()
            return redirect('view_address')
    else:
            address = Address.objects.get(pk=id, user=request.user)
            address_form = UserAddressForm(instance=address)

    return render(request,'edit_address.html',{'form':address_form})

def delete_address(request,id):

    address = Address.objects.filter(pk=id,user=request.user).delete()
    return redirect('view_address')