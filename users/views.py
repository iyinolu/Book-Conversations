from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.views import logout_then_login
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

def logout(request):
    return logout_then_login(request)
        
            




## TEST AREA
from .forms import FormExp


def form_exp(request):
    if request.method == 'POST':
        form = FormExp(request.POST)
        if form.is_valid():
            pass
        pass
    else:
        form = FormExp()

    return render(request, 'users/form_exp.html', {'form':form})