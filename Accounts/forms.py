from django import forms
from.models import Account

class BudgetAccountRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'text-field-2 w-input', 'placeholder': '**********'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'text-field-2 w-input', 'placeholder': '**********'}))

    class Meta:
        model = Account
        fields = ['email']

class StudentAccountRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'text-field-2 w-input', 'placeholder': '**********'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'text-field-2 w-input', 'placeholder': '**********'}))

    class Meta:
        model = Account
        fields = ['email']

