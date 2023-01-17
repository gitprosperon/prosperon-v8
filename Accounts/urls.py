from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register-budget', views.register_budget_account, name='register-budget'),

]
