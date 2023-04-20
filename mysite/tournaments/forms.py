from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SearchForm(forms.Form):
    query = forms.CharField(label='Find tournaments containing:', max_length=100)

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2"]