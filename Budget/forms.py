from django import forms
from .models import Goal, MonthlySummary


class AddGoalForm(forms.ModelForm):

    class Meta:
        model = Goal
        fields = ['title', 'user', 'cost']


class UpdateChangedTransactions(forms.ModelForm):

    class Meta:
        model = MonthlySummary
        fields = ['account_transactions']