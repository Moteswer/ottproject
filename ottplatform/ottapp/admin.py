from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('firstname','username', 'password', 'email','phonenumber')  # Customize the fields you want to display
    # Add other configurations as needed
