from django.urls import path
from . import views


urlpatterns = [
    path('meta/', views.display_meta, name='meta-info'),
    path('category-add/', views.add_category, name='add-category'),
    path('', views.landing_page, name='landing-page'),
    path('book-add/', views.create_book, name='add-book'),
    path('show-books/<int:id>', views.test_showbook, name='show-category'),
    path('show-category/', views.test_view, name='category-list')
]