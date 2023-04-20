from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Find tournaments containing:', max_length=100)