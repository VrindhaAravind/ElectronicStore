from django.shortcuts import render,redirect
from .forms import UserForm,ProfileForm
from .models import Seller_Details



# Create your views here.

def register(request):
    user_form = UserForm(request.POST)
    profile_form = ProfileForm(request.POST)
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
            
        return render(request,'seller_registration.html',{'user_form':user_form,'profile_form':profile_form})
    return render(request, 'seller_registration.html', {'user_form': user_form, 'profile_form': profile_form})