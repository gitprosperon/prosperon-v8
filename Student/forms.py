from django import forms
from .models import Student, BudgetItemsUniversity


class UpdateProgressForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['course_progress']


class AddBudgetForm(forms.ModelForm):

    class Meta:
        model = BudgetItemsUniversity
        fields = ['user', 'category', 'total_per_month', 'users_id']



