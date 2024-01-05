# forms.py
from django import forms
from .models import Customer

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'email', 'username', 'password', 'DoB', 'phonenumber']
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
