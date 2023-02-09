from django import forms
from.models import Account
from Student.models import Student
from django.contrib.auth.forms import AuthenticationForm


# Registration for budgeting account
class BudgetAccountRegistrationForm(forms.ModelForm):
    email = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'text-field w-input', 'id': 'email'}))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'text-field w-input', 'placeholder': '**********'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'text-field w-input', 'placeholder': '**********'}))

    class Meta:
        model = Account
        fields = ['email']

# Account registration for students
class StudentAccountRegistrationForm(forms.ModelForm):
    email = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'text-field w-input', 'id': 'email'}))

    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'class': 'text-field w-input', 'placeholder': '**********'}))
    password2 = forms.CharField(label='Repeat password', required=True, widget=forms.PasswordInput(attrs={'class': 'text-field w-input', 'placeholder': '**********'}))

    class Meta:
        model = Account
        fields = ['email']

# Account registration for DTC
class DtcAccountRegistrationForm(forms.ModelForm):
    email = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'text-field w-input', 'id': 'email'}))

    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'class': 'text-field w-input', 'placeholder': '**********'}))
    password2 = forms.CharField(label='Repeat password', required=True, widget=forms.PasswordInput(attrs={'class': 'text-field w-input', 'placeholder': '**********'}))

    class Meta:
        model = Account
        fields = ['email']

# Form for adding student model
class AddStudentAccountForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['user_id_number', 'course_progress', 'student_email', 'life_path', 'total_points', 'last_points_added']

# Form for adding profile image
class AddProfileImage(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['user_image']

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'text-field w-input', 'id': 'email'}))
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'class': 'text-field w-input', 'placeholder': '**********'}))

