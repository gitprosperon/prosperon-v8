from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "MainWebsitte"

urlpatterns = [
    path('', views.home_page, name='home_page'),  # Home page
    path('all-blogs', views.all_blogs, name='all_blogs'),  # Blogs page
    path('blog/<str:id>', views.blog, name='blog'),  # Blogs page

]
