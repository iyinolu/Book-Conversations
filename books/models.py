from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import ModelState
from django.db.models.deletion import SET_NULL
from django.utils import timezone


# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f'Publisher: {self.name}'

class Author(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    profile_image = models.ImageField(default='default.png', upload_to='auuthor_pictures')
 
    def __str__(self):
        return f'Author: {self.first_name}'

class Category(models.Model):
    category_name = models.CharField(max_length=40)
    description = models.TextField(max_length=200)
    
    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Category'

class Book(models.Model):
    posted_by = models.OneToOneField(User, on_delete=models.deletion.DO_NOTHING, default=0)
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author, related_name='author')
    publisher = models.ForeignKey(Publisher, blank=True, null=True, on_delete=models.SET_NULL)
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Category')

    def __str__(self):
        return f'Book: {self.title}'



