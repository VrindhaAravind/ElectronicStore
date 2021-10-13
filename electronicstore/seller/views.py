from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.models import User, auth
from django.http import HttpResponse

# Create your views here.

def login(request):
    if request.method=='POST':
        # print(request.POST.get('username'),request.POST.get('password'))
        id=User.objects.get(username=request.POST.get('username')).pk
        # print(id)
        if models.Seller_Details.objects.filter(username =request.POST.get('username')).exists():
            print('user exist')
            print(models.Seller_Details.objects.get(username ='manu').user)
            user=auth.authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                return render(request,'seller_login.html')
    return render(request,'seller_login.html')

def home(request):
    return HttpResponse('Welcome Home')

def products(request):
    s=request.user
    print(s)
    products=models.Products.objects.filter(user=request.user)

    return render(request,'seller_view_product.html',{'products':products})

def products_edit(request):
    if request.method == 'POST':
        x=request.POST.get('prod_id')
        prod=models.Products.objects.get(id=x)
        print(x,prod.product_name)
        return render(request,'prod_edit.html',{'prod':prod})
    return HttpResponse('lets edit')

def products_edit_confirm(request):
    req=request.POST
    if request.method == 'POST':
        print(request.POST.get('prod_id'))
        prod=models.Products.objects.get(id=request.POST.get('prod_id'))
        prod.product_name=req.get('prod_name')
        prod.description=req.get('prod_description')
        prod.stock=req.get('prod_stock')
        prod.price=req.get('prod_price')
        prod.ram=req.get('prod_ram')
        prod.storage=req.get('prod_storage')
        prod.color=req.get('prod_color')
        prod.offer=req.get('prod_offer')
        print(request.POST.get('prod_name'),prod.product_name)
        prod.save()
        # prod.product_name = request.POST.get('')
        s = request.user
        print(s)
        products = models.Products.objects.filter(user=request.user)
        print(request.build_absolute_uri('/products/'))
        return redirect(request.build_absolute_uri('/products/'))



from .forms import UserForm,ProfileForm

def register(request):
    user_form = UserForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)
    if request.method == "POST":

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            profile = profile_form.save(commit=False)

            profile.user = user
            profile.username = user.username
            profile.save()

            return redirect('base')

        else:

            user_form = UserForm()
            profile_form = ProfileForm()

        return render(request, 'seller_registration.html', {'user_form': user_form, 'profile_form': profile_form})
    return render(request, 'seller_registration.html', {'user_form': user_form, 'profile_form': profile_form})