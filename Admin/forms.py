from django import forms
from Student.models import Location, Apartment, Job

class AddLocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ['city', 'average_rent']


class AddApartmentForm(forms.ModelForm):

    class Meta:
        model = Apartment
        fields = '__all__'

class OriginalJobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['original']


class CreateNewJobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = '__all__'