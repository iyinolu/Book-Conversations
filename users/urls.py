from django.contrib.auth import views as auth_views
from django.urls import path
from .views import form_exp, register, logout
# from .views import form_exp

urlpatterns = [
    path('register/', register, name='register-view'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), 
        name='login-view'),
    path('logout/', logout, name='logout-view'),
    path('exp/', form_exp, name='exp')
]