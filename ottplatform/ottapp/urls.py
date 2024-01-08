from django.contrib import admin
from django.urls import path, include
from .views import ProfileDetailView, create_profile, home_view, kid_profile_registration_view, list_profiles, profile_registration_view, register_customer,login_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_customer, name='register_customer'),
    path('login/', login_view, name='login'), 
    path('create_profile/', create_profile, name='create_profile'),
    path('list_profiles/<int:customer_id>/', list_profiles, name='list_profiles'),
    path('profile/<int:customer_id>/', profile_registration_view, name='profile_registration'),
    path('profile/detail/<int:customer_id>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('customer/<int:customer_id>/kid-profile-registration/', kid_profile_registration_view, name='kid_profile_registration'),
]
