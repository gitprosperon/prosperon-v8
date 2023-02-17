from django import forms
from Student.models import Location, Apartment
from .models import ContactModelForm

class AddLocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ['city']

class AddApartmentForm(forms.ModelForm):

    class Meta:
        model = Apartment
        fields = ['title']



class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactModelForm
        fields = ['name', 'email', 'message']