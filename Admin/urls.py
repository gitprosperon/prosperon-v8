from django.urls import path
from Admin import views

app_name = "Admin"


urlpatterns = [
    # Sidebar Pages
    path('create-locations', views.create_lcoations, name='create-locations'),
    path('create-apartments', views.addAllApartments, name='create-apartments'),

]