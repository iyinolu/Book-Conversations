from django.urls import path
from .views import display_meta, add_category, show_category, test_bookform
from . import views


urlpatterns = [
    path('meta/', display_meta, name='meta-info'),
    path('category-add/', add_category, name='add_category'),
    path('category-show/', show_category, name='show_category'),
    path('test_bookform/', views.BookCreateView.as_view(), name='test_bookf'),
]