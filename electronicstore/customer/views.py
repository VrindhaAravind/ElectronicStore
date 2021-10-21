from django.shortcuts import render, redirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView
from .forms import RegistrationForm,LoginForm,UpdateForm,ReviewForm,PlaceOrderForm,UserAddressForm,UserForm
from .models import Cart,Review,Orders,Address,Userdetails
from seller.models import Products
from .decorators import signin_required
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.db.models import IntegerField, Case, Value, When
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
class HomePageView(ListView):
    template_name = 'homepage.html'
    model = Products
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        products = Products.objects.all()
        paginator = Paginator(products, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            page_products = paginator.page(page)
        except PageNotAnInteger:
            page_products = paginator.page(1)
        except EmptyPage:
            page_products = paginator.page(paginator.num_pages)

        context['products'] = page_products
        return context

def search(request):
    search = request.GET['q']
    product = Products.objects.filter(product_name__icontains=search)
    context = {'product': product}
    return render(request, 'search.html', context)

@signin_required
def signout(request):
    logout(request)
    return redirect("cust_signin")


@signin_required
def mobiles(request):
    mobiles = Products.objects.filter(category='mobile')
    context = {'mobiles': mobiles}
    return render(request, 'category.html', context)
@signin_required
def laptops(request):
    laptops = Products.objects.filter(category="laptop")
    context = {'laptops': laptops}
    return render(request, 'category.html', context)
@signin_required
def tablets(request):
    tablets = Products.objects.filter(category="tablet")
    context = {'tablets': tablets}
    return render(request, 'category.html', context)
@signin_required
def price_low_to_high(request):
    low = Products.objects.all().order_by('price')
    context = {'low': low}
    return render(request, 'price_range.html', context)
@signin_required
def price_high_to_low(request):
    high = Products.objects.all().order_by('-price')
    context = {'high': high}
    return render(request, 'price_range.html', context)

@signin_required
def apple(request):
    apple = Products.objects.filter(brand='apple')
    context = {'apple': apple}
    return render(request, 'category.html', context)

@signin_required
def lenovo(request):
    lenovo = Products.objects.filter(brand='lenovo')
    context = {'lenovo': lenovo}
    return render(request, 'category.html', context)

@signin_required
def oppo(request):
    oppo = Products.objects.filter(brand='oppo')
    context = {'oppo': oppo}
    return render(request, 'category.html', context)

@signin_required
def oneplus(request):
    oneplus = Products.objects.filter(brand='oneplus')
    context = {'oneplus': oneplus}
    return render(request, 'category.html', context)

@signin_required
def redmi(request):
    redmi = Products.objects.filter(brand='redmi')
    context = {'redmi': redmi}
    return render(request, 'category.html', context)

@signin_required
def samsung(request):
    samsung = Products.objects.filter(brand='samsung')
    context = {'samsung': samsung}
    return render(request, 'category.html', context)

# @method_decorator(signin_required, name="dispatch")
def ViewDetails(request):
    dets=Userdetails.objects.filter(user=request.user)
    return render(request,'my_profile.html',{'dets':dets})

class EditDetails(TemplateView):
    user_form = UserForm
    profile_form = UpdateForm
    template_name = "user_details.html"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = UpdateForm(post_data, file_data, instance=request.user)
        #profile_form = UpdateForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse_lazy('view_profile'))

        context = self.get_context_data(user_form=user_form, profile_form=profile_form)

        return self.render_to_response(context)




@method_decorator(signin_required, name="dispatch")
class ViewProduct(TemplateView):
    template_name = 'productdetail.html'
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        product = Products.objects.get(id=id)
        reviews = Review.objects.filter(product=product)
        similar_products=Products.objects.filter(brand=product.brand,category=product.category)
        self.context['product'] = product
        self.context['reviews'] = reviews
        self.context['similar_products']=similar_products
        return render(request, self.template_name, self.context)
@signin_required
def add_to_cart(request, *args, **kwargs):
    id = kwargs['pk']
    product = Products.objects.get(id=id)
    cart = Cart(product=product, user=request.user)
    cart.save()
    return redirect('mycart')

@method_decorator(signin_required, name="dispatch")
class MyCart(TemplateView):
    template_name = 'cart.html'
    context = {}

    def get(self, request, *args, **kwargs):
        cart_products = Cart.objects.filter(user=request.user, status='ordernotplaced')
        self.context['cart_products'] = cart_products
        return render(request, self.template_name, self.context)

@method_decorator(signin_required, name="dispatch")
class DeleteFromCart(TemplateView):
    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        cart_product = Cart.objects.get(id=id)
        cart_product.delete()
        return redirect('mycart')


@method_decorator(signin_required, name="dispatch")
class WriteReview(TemplateView):
    template_name = 'review.html'
    context = {}

    def get(self, request, *args, **kwargs):
        form = ReviewForm()
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs['id']
        product = Products.objects.get(id=id)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.cleaned_data.get('review')
            new_review = Review(user=request.user, product=product, review=review)
            new_review.save()
            return redirect('viewproduct', product.id)
@signin_required
def place_order(request, *args, **kwargs):
    print(kwargs)
    id = kwargs.get("id")
    product = Products.objects.get(id=id)
    address = Address.objects.filter(user=request.user)
    
    instance = {
        "product": product.product_name,
        'address': address,

    }
    # print(instance)
    form = PlaceOrderForm(initial=instance)

    context = {}
    context["form"] = form

    if request.method == "POST":
        cid = kwargs.get("cid")

        cart = Cart.objects.get(id=cid)



        address = request.POST.get('radioaddress')

        print(address)
        product = product
        order = Orders(product=product, user=request.user, seller=product.user.username, address=address)
        print(order)
        order.save()

        cart.status = "orderplaced"
        cart.save()

        return redirect("customer_home")

    return render(request, "placeorder.html", {'address': address, 'product': product})
@signin_required
def view_orders(request,*args,**kwargs):
    orders=Orders.objects.filter(user=request.user)

    context={
        "orders":orders,
    }
    print(kwargs)
    return render(request,"vieworders.html",context)
@signin_required
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