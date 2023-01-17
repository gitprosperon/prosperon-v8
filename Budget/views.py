from django.shortcuts import render, redirect
from .models import Goal, BudgetItems
import json
import environ
from Accounts.models import Account
from Budget.models import BankAccount
import requests

# creating env object
env = environ.Env()
# reading .env file
environ.Env.read_env()

# plaid information
CLIENT_ID = env("CLIENT_ID")
SECRET = env("SECRET")



# add an account
def addAccount(request):
    user = request.user
    if user.is_active and user.has_budget == True:
        account = Account.objects.filter(pk=request.user.pk)
        user_id = account.model.get_user_id(self=user)

        # Creating link token
        url = 'https://development.plaid.com/link/token/create'

        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            "client_id": F"{CLIENT_ID}",
            "secret": f"{SECRET}",
            "user": {"client_user_id": f"{user_id}"
                     },
            "client_name": "ProsperOn",
            "products": ["auth"],
            "country_codes": ["US"],
            "language": "en",
            "webhook": "https://www.prosperon-university.com/",
            "redirect_uri": "https://www.prosperon-university.com/oauth.html",

        }

        r = requests.post(url, headers=headers, json=data)
        linkToken = r.json()['link_token']

        print(linkToken)

        context = {
            'linkToken': linkToken,
        }

        return render(request, 'Budget/add_account.html', context=context)


# Authenticaction for plaid
def oauth(request):
    user = request.user
    if request.POST.get('action') == 'post':
        print('this is accounts test')


    return render(request, 'Budget/o-auth.html')


# Budget Dashboard
def budget_dashboard(request):
    user = request.user
    if user.is_active and user.has_budget == True:
        account = Account.objects.filter(pk=request.user.pk)
        user_id = account.model.get_user_id(self=user)
        bank_accounts = BankAccount.objects.filter(users_id=user_id)
        goals = Goal.objects.filter(users_id=user_id)

        # receiving AJAX from changing a transaction category
        if request.POST.get('action') == 'post':
            public = request.POST
            print(public)


        # Getting all accounts
        for account in bank_accounts:
            token = account.token
            print('ads4tfg3433')
            url = 'https://development.plaid.com/transactions/get'
            headers = {
                'Content-Type': 'application/json'
            }
            data = {
                "client_id": F"{CLIENT_ID}",
                "secret": f"{SECRET}",
                "access_token": f'{token}',
                "start_date": "2022-11-02",
                "end_date": "2023-11-04",
                "options": {
                    "count": 3,
                    "offset": 0
                }
            }

            # Transaction data received
            transaction_data = requests.post(url, headers=headers, json=data).json()['transactions']
            print(transaction_data)






    context = {
        'transaction_data': transaction_data,
        'goals': goals
    }



    return render(request, 'Budget/dashboard.html', context=context)


# Goals page
def goals(request):
    user = request.user
    account = Account.objects.filter(pk=request.user.pk)
    user_id = account.model.get_user_id(self=user)

    if user.is_active and user.has_budget == True:
        my_goals = Goal.objects.filter(user=request.user)


        context = {
            'myGoals': my_goals,

        }

        return render(request, 'Budget/Goals/goals.html', context=context)

    else:
        return render(request, 'MainWebsite/index.html')


# Page to add goals
def add_goals(request):
    user = request.user
    account = Account.objects.filter(pk=request.user.pk)
    user_id = account.model.get_user_id(self=user)

    if user.is_active and user.has_budget == True:
        my_goals = Goal.objects.filter(user=request.user)

        if request.method == 'POST':
            print(request.POST)


        context = {
            'test': my_goals
        }

        return render(request, 'Budget/Goals/add_goal.html', context=context)

    else:
        return render(request, 'MainWebsite/index.html')


# View individual goal
def view_goal(request, id):
    user = request.user
    if user.is_active and user.has_budget == True:
        goal = Goal.objects.get(pk=id)
        title = goal.title
        currentAmount = goal.current_amount
        totalAmount = goal.cost
        image = goal.image
        print(image)

        context = {
            'title': title,
            'currentAmount': currentAmount,
            'totalAmount': totalAmount,
            'image': image,

        }

        return render(request, 'Budget/Goals/view_goal.html', context=context)


# Transactions page
def transactions(request):
    user = request.user
    if user.is_active and user.has_budget == True:
        account = Account.objects.filter(pk=request.user.pk)
        user_id = account.model.get_user_id(self=user)
        my_goals = Goal.objects.filter(user=request.user)


        context = {
            'myGoals': my_goals,

        }

        return render(request, 'Budget/transactions.html', context=context)

    else:
        return render(request, 'MainWebsite/index.html')


# budget page
def budget(request):
    user = request.user
    if user.is_active and user.has_budget == True:
        account = Account.objects.filter(pk=request.user.pk)
        user_id = account.model.get_user_id(self=user)
        all_budgets = BudgetItems.objects.filter(users_id=user_id)
        print(all_budgets)


        context = {
            'all_budgets': all_budgets,

        }

        return render(request, 'Budget/budget.html', context=context)

    else:
        return render(request, 'MainWebsite/index.html')

def add_budget(request):
    return render(request, 'Budget/add_budget.html')


# accounts page
def accounts(request):
    user = request.user
    if user.is_active and user.has_budget == True:

        return render(request, 'Budget/accounts.html')


# notifications page
def notifications(request):
    user = request.user
    if user.is_active and user.has_budget == True:
        if request.POST.get('action') == 'post':
            public = request.POST
            print(public)

        return render(request, 'Budget/notifications.html')