from django.urls import path
from .views import display_meta, add_category, show_category, test_bookform
from . import views


urlpatterns = [
    path('meta/', display_meta, name='meta-info'),
    path('category-add/', add_category, name='add-category'),
    path('', show_category, name='home-view'),
    path('test_bookform/', views.create_book, name='test_book'),
    path('test_showbook/<int:id>', views.test_showbook, name='show-category')
]