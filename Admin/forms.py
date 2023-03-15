from django import forms
from Student.models import Location, Apartment

class AddLocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ['city', 'average_rent']


class AddApartmentForm(forms.ModelForm):

    class Meta:
        model = Apartment
        fields = '__all__'