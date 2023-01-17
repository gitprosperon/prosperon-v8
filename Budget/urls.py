from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "Budget"


urlpatterns = [
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

    # accounts
    path('accounts', views.accounts, name='budget-accounts'),
    path('add-account', views.addAccount, name='budget-addAccount'),

    # notifications
    path('notifications', views.notifications, name='budget-notifications'),

    # Plaid Authentication
    path('o-auth', views.oauth, name='budget-oauth'),

]
