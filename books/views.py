from django.http.request import validate_host
from django.shortcuts import render
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

def test_bookform(request):
    form = BookForm()
    context = {'author':form}

    return render(request, 'books/test_bookform.html', context)

class BookCreateView(CreateView):
    model = models.Book
    form_class = forms.BookForm
    success_url = reverse_lazy("landing-page")

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)
        
def test_showbook(request):
    return render(request, 'books/test_showbook.html', context={'n':range(10)})