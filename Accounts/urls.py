from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "Accounts"


urlpatterns = [
    path('register-budget', views.register_budget_account, name='register-budget'),
    path('register-student', views.register_student_account, name='register-student'),
    path('register-dtc', views.register_dtc_account, name='register-dtc'),
    path('logout', views.logout, name='logout'),
    path('login', views.LoginUser.as_view(), name='login_student'),

    path('registration-choice', views.register_choice, name='registration-choice'),


]
