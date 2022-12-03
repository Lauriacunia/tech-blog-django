from django import forms
from django.forms import  PasswordInput, TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={'class': 'input is-info',
                                     'placeholder': 'Username'}),
            'email': TextInput(attrs={'class': 'input is-info',
                                      'placeholder': 'Email'}),
            'password1': PasswordInput(attrs={'class': 'input is-info',
                                        'placeholder': 'Password'}),
            'password2': PasswordInput(attrs={'class': 'input is-info',
                                        'placeholder': 'Confirm Password'}),
        }

class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': TextInput(attrs={'class': 'input is-info',
                                     'placeholder': 'Username'}),
            'first_name': TextInput(attrs={'class': 'input is-info',
                                        'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'class': 'input is-info',
                                        'placeholder': 'Last Name'}),
            'email': TextInput(attrs={'class': 'input is-info',
                                        'placeholder': 'Email'}),
        }