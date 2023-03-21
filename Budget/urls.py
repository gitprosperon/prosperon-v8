from django.contrib import admin
from django.urls import path, include
from . import views, functions


app_name = "Budget"


urlpatterns = [

    # Refresh
    path('refresh', views.refresh, name='budget-refresh'),

    # dashboard
    path('dashboard', views.budget_dashboard, name='budget-dashboard'),

    # Goals
    path('goals', views.goals, name='budget-goals'),
    path('add-goals', views.add_goals, name='budget-addGoals'),
    path(r'my-goal/<str:id>', views.view_goal, name='budget-viewGoals'),

    # transactions
    path('transactions', views.transactions, name='budget-transactions'),

    # Budget
    path('budget', views.budget, name='budget-budget'),
    path('add-budget', views.add_budget, name='add-budget'),
    path('generate-budget', functions.create_budget, name='generate-budget'),
    path('view-budget/<str:id>', views.view_budget, name='view-budget'),
    path('delete-budget/<str:id>', views.delete_budget, name='delete-budget'),

    # accounts
    path('accounts', views.accounts, name='budget-accounts'),
    path('add-account', views.addAccount, name='budget-addAccount'),

    # notifications
    path('notifications', views.notifications, name='budget-notifications'),

    # Plaid Authentication
    path('o-auth', views.oauth, name='budget-oauth'),


]
