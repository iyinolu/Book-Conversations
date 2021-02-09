from django.contrib.admin.widgets import AutocompleteSelectMultiple
from django import forms
from django.db.models import fields
from django.contrib import admin
from django.forms import widgets 
from django_select2 import forms as s2forms
from .models import Author, Book, Category, Publisher

class AuthorWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        'first_name__icontains',
        'last_name__icontains',
    ]

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'city']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email', 'profile_image']



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'category']
        widgets = {
            'author': AuthorWidget
        }