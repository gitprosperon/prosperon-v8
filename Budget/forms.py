from django import forms
from .models import Goal


class AddGoalForm(forms.ModelForm):

    class Meta:
        model = Goal
        fields = ['title', 'user', 'cost']