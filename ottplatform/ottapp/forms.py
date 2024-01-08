# forms.py
from django import forms
from .models import Customer
from .models import CustomerProfile, KidProfile

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['profilename']

class KidProfileForm(forms.ModelForm):
    class Meta:
        model = KidProfile
        fields = ['profilename', 'avatar']


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'email', 'username', 'password', 'DoB', 'phonenumber']
        widgets = {
            'password': forms.PasswordInput(),
            'DoB': forms.DateInput(attrs={'type': 'date'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['profilename','pin']

