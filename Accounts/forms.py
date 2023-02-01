from django import forms
from.models import Account
from Student.models import Student

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

class AddStudentAccountForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['user_id_number', 'course_progress', 'student_email', 'life_path', 'total_points', 'last_points_added']

