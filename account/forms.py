from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)

class RegForm(UserCreationForm):
    phone_number=forms.CharField(max_length=15, required=True, help_text='Enter a valid phone number.')
    class Meta:
        model=User
        fields=["first_name","last_name","phone_number","email","username","password1","password2"]
