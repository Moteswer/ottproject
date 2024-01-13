from django.contrib import admin
from django.urls import path, include
from .views import  MovieKidDetail, MovieListView, Moviedetail, ProfileDetailView, Random, admin_dashboard, admin_login_view, all_movies, delete_kid_profile, delete_profile, go_back, go_to_login,  kidmovie_list,kidprofile_details, home_view, kid_profile_registration_view, list_profiles, logout_view, movie_list, profile_details, profile_registration_view, random_details, register_customer,login_view,KidMovieListView, select_subscription_plan, upcoming_movies, update_kid_profile, update_profile

urlpatterns = [
    path('home/', home_view, name='home'),
    path('register', register_customer, name='register_customer'),
    path('', login_view, name='login'),
    path('admin-login/', admin_login_view, name='admin_login'),
    path('admin/', admin_dashboard, name='admin_dashboard'),
    path('list_profiles/<int:customer_id>/', list_profiles, name='list_profiles'),
    path('profile/<int:customer_id>/', profile_registration_view, name='profile_registration'),
    path('profile/detail/<int:customer_id>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('customer/<int:customer_id>/kid-profile-registration/', kid_profile_registration_view, name='kid_profile_registration'),
    path('profile/detail/<int:customer_id>/profile/<int:profile_id>/', profile_details, name='profile_details'),
    path('profile/detail/<int:customer_id>/kidprofile/<int:profile_id>/', kidprofile_details, name='kidprofile_details'),
    path('movies/<int:profile_id>/', MovieListView.as_view(), name='movie_list'),
    path('movie_detail/<int:id>/',Moviedetail.as_view(), name='movie_detail'),
    path('kidmovielist/<int:id>/', KidMovieListView.as_view(), name='kidmovielist'),
    path('moviekiddetail/<int:id>/', MovieKidDetail.as_view(), name='moviekiddetail'),
    path('upcoming_movies/<int:movie_id>/', upcoming_movies, name='upcoming_movies'),
    path('movies/',movie_list,name='movie_list'),
    path('kidmovies/',kidmovie_list,name='kidmovie_list'),
    path('update_profile/<int:customer_id>/<int:profile_id>/', update_profile, name='update_profile'),
    path('delete_profile/<int:customer_id>/<int:profile_id>/', delete_profile, name='delete_profile'),
    path('update_kid_profile/<int:customer_id>/<int:kid_profile_id>/', update_kid_profile, name='update_kid_profile'),
    path('delete_kid_profile/<int:customer_id>/<int:kid_profile_id>/', delete_kid_profile, name='delete_kid_profile'),
    path('logout/', logout_view, name='logout'),
    path('select-subscription-plan/<int:customer_id>/', select_subscription_plan, name='select_subscription_plan'),
    path('go-to-login/', go_to_login, name='go_to_login'),
    path('go_back/',go_back,name = 'go_back'),
    path('random_movies/<int:id>/',Random.as_view() , name='random_movies'),
    path('random_details/',random_details,name='random_details'),
    path('all_movies/', all_movies, name='all_movies'),

  
]
