# ottplatform/urls.py
from django.contrib import admin
from django.urls import path, include  # Import the necessary view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ottapp.urls')),
  # Include ottapp URLs under /ottapp/
    # Add other app-specific URLs here
]
