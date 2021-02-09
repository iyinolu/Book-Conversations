from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import *

# Create your views here.
def test(request):
    return render(request, "users/home_temp.html")

def register(request):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, {username}!')
            return redirect('login-view')
    else:
        user_form = UserRegisterForm()
    return render(request, "users/register.html", {'user_form':user_form})
        
            
