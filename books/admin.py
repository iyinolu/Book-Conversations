from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import *


ADMIN = AdminSite

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')

class PublishAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'description')
    


# Register your models here.
admin.site.register(Publisher, PublishAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)