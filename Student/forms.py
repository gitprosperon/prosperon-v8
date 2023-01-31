from django import forms
from .models import Student, BudgetItemsUniversity, ModuleSummarie


class UpdateProgressForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['course_progress']



class AddBudgetForm(forms.ModelForm):

    class Meta:
        model = BudgetItemsUniversity
        fields = ['user', 'title', 'category', 'total_per_month', 'users_id']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input budget w-input', 'placeholder': 'Title'}),
            'total_per_month': forms.TextInput(attrs={'class': 'input budget w-input', 'placeholder': 'Total Per Month'}),
            'category': forms.Select(choices=BudgetItemsUniversity.CATAGORIES, attrs={'class': 'input budget w-input', 'name': 'Total Per Month', 'data-name': 'Category'})

        }


class NewModuleSummaryForm(forms.ModelForm):

    class Meta:
        model = ModuleSummarie
        fields = ['user', 'users_id', 'module_url', 'module']