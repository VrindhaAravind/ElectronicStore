from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Seller_Details,Products

class UserForm(UserCreationForm):
    username = forms.CharField(max_length=15, widget=(
        forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'})))
    first_name = forms.CharField(max_length=15, widget=(
        forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'})))

    password1 = forms.CharField(max_length=20, label="Password", widget=(
        forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})))
    password2 = forms.CharField(max_length=20, label="Confirm-Password", widget=(
        forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})))
    email = forms.CharField(max_length=100,
                            widget=(forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'})))
    class Meta:
        model = User
        fields = ['first_name','username','email','password1','password2']


class ProfileForm(forms.ModelForm):

    address = forms.CharField(max_length=500,widget=(forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter address'})))
    bank_name = forms.CharField(max_length=50,
                             widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bank Name'})))
    account_number = forms.CharField(max_length=50,
                                widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Account-Number'})))
    ifsc_code = forms.CharField(max_length=15,
                                     widget=(forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'Enter IDSC Code'})))


    class Meta:
        model = Seller_Details
        fields = ['address','bank_name','account_number','ifsc_code']

