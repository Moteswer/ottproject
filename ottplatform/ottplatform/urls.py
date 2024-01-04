# ottplatform/urls.py
from django.contrib import admin
from django.urls import path, include
from ottapp.views import login_view  # Import the necessary view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ottapp.urls')),
    path('login/', login_view, name='login'),   # Include ottapp URLs under /ottapp/
    # Add other app-specific URLs here
]
