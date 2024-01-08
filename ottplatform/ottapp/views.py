# views.py
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateProfileForm, CustomerRegistrationForm
# ottapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from .models import Customer, CustomerProfile
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, CustomerProfile, KidProfile
from .forms import CustomerProfileForm, KidProfileForm

def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                customer = Customer.objects.get(username=username)
                if customer.password == password:
                    # Get the customer ID and redirect to the profile detail page
                    customer_id = customer.id
                    return redirect('profile_detail', customer_id=customer_id)
                else:
                    form.add_error(None, 'Invalid credentials')
            except Customer.DoesNotExist:
                form.add_error(None, 'User not found')

    return render(request, 'user/login.html', {'form': form})






def home_view(request):
    return render(request, 'home.html')



def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page 
    else:
        form = CustomerRegistrationForm()

    return render(request, 'registration.html', {'form': form})


def profile_list(request):
    # Assuming the user is logged in and has a related customer object
    if request.user.is_authenticated:
        customer = request.user.customer  # Assuming a one-to-one relationship between User and Customer
        profiles = CustomerProfile.objects.filter(customer=customer)
        return render(request, 'user/profile_list.html', {'profiles': profiles})
    else:
        # Handle the case where the user is not authenticated (e.g., redirect to login)
        return render(request, 'error.html', {'error_message': 'User is not authenticated'})

def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = CreateProfileForm()

    return render(request, 'user/create_profile.html', {'form': form})


def profile_registration_view(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    template_name = 'profile_registration.html'

    if request.method == 'POST':
        profile_form = CustomerProfileForm(request.POST)

        print(profile_form.is_valid())  # Check if the form is valid
        print(profile_form.errors)       # Print form errors if any

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.customer = customer
            profile.save()

            return redirect('profile_detail', customer_id=customer.id)

    else:
        profile_form = CustomerProfileForm()

    return render(request, template_name, {'customer': customer, 'profile_form': profile_form})


class ProfileDetailView(View):
    template_name = 'profile_detail.html'

    def get(self, request, customer_id):
        customer = Customer.objects.get(id=customer_id)
        profile = customer.profile.all()  # Assuming there's only one profile per customer
        kid_profiles = customer.kid_profiles.all()
        return render(request, self.template_name, {'customer': customer, 'profile': profile, 'kid_profiles': kid_profiles})
    

def list_profiles(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    profiles = customer.customerprofile.all()  # Assuming your profile model is named CustomerProfile

    return render(request, 'profile_list.html', {'customer': customer, 'profiles': profiles})