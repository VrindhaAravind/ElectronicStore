from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from customer.forms import RegistrationForm,LoginForm


class RegistrationView(TemplateView):
<<<<<<< HEAD
    form_class=RegistrationForm
    template_name="registration.html"
    model=User
    context={}

    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
=======
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    model = User
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
>>>>>>> 1b5d59eb531923428a3327cace5c5c696dd49e79
        if form.is_valid():
            form.save()

            return redirect("cust_signin")



class SignInView(TemplateView):
<<<<<<< HEAD
    template_name="login.html"
    form_class=LoginForm
    context={}
=======
    template_name = "login.html"
    form_class = forms.LoginForm
    context = {}
>>>>>>> 1b5d59eb531923428a3327cace5c5c696dd49e79

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
<<<<<<< HEAD
                self.context["form"]=form
                return render(request,self.template_name,self.context)

class HomePageView(TemplateView):
    template_name = 'homepage.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)
=======
                self.context["form"] = form
                return render(request, self.template_name, self.context)


def signout(request):
    logout(request)
    return redirect("signin")
>>>>>>> 1b5d59eb531923428a3327cace5c5c696dd49e79
