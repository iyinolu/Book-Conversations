from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """Form to create new user"""
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileRegisterForm(ModelForm):
    """Form to allow user add profile 
    related data E.g. profile-image
    """
    class Meta:
        model = Profile
        fields = ['profile_picture']

    