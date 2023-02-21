from django.contrib import admin
from django.urls import path, include
from . import views
from . import tool_views

app_name = "MainWebsitte"

urlpatterns = [
    path('', views.home_page, name='home_page'),  # Home page
    path('our-story', views.our_stpry, name='our-story'),  # Our story page
    path('product', views.product_page, name='product'),  # Our story page
    path('pilot-program', views.pilot_program_page, name='pilot-program'),  # Our story page
    path('pilot-program', views.pilot_program_page, name='pilot-program'),  # Our story page
    path("testimonials", views.testamonials, name='testimonials'),
    path('all-blogs', views.all_blogs, name='all_blogs'),  # Blogs page
    path('blog/<str:id>', views.blog, name='blog'),  # Blogs page

    path('terms-and-conditions', views.terms_and_conditions, name='terms-and-conditions'),  # Our story page

    # TOOL PAGES
    path("mortgage-calculator", tool_views.mortgage_calculator, name='mortgage-calculator'),
    path("tool/<str:id>", tool_views.tool_page, name='mortgage-calculator'),

]
