from django.shortcuts import render
from Student.models import Location
from .forms import AddLocationForm, AddApartmentForm





# Create your views here.
def home_page(request):


    return render(request, 'MainWebsite/index.html')