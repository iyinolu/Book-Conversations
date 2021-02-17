from django.http.request import validate_host
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import AuthorForm, BookForm, CreateCategoryForm
from .models import Category

from django.views.generic import CreateView
from . import forms, models

# Create your views here.

def display_meta(request):
    """Inspect request information"""
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def add_category(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing-page')
               
    form = CreateCategoryForm()
    return render(request, 'books/create_category.html', {'form': form})
 
def show_category(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    return render(request, 'books/homepage.html', context)

def test_bookform(request, *args, **kwargs):
    form = BookForm(request.POST, request.FILES, instance=request.user.profile)
    context = {'author':form}

    if form.is_valid:
        form.save()
    return render(request, 'books/test_bookform.html', context)

class BookCreateView(CreateView):
    fields = '__all__'
    template_name = 'books/book_form.html'
    

    def get(self, request, *args, **kwargs):
        form = forms.BookForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect("home-view")

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


def create_book(request):
    if request.method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        form.instance.posted_by = request.user

        if form.is_valid():
            form.save()
        return redirect('home-view')
    else:
        
        form = BookForm()
    return render(request, 'books/book_form.html', context={'form':form})













        
def test_showbook(request, id=None):
    if id:
        books = models.Book.objects.filter(category_id=id).all()
        cate_name = models.Category.objects.filter(id=id).first().category_name
        context = {'books': books, 'name':cate_name}
    else:
        context = {}
        
    return render(request, 'books/test_showbook.html', context)
