from django.contrib import admin
from django.urls import path, include
from .views import home_view, register_customer,login_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_customer, name='register_customer'),
    path('login/', login_view, name='login'),
    # Add other app-specific URLs here
]
