from django import forms
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.models import User

class UserRegister(UserCreationForm):
    email=forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model=User
        fields=['email', 'username', 'password1', 'password2']

class UserLoginform(AuthenticationForm):
    username=forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))