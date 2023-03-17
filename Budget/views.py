from django.shortcuts import render, redirect
from .models import Goal, BudgetItems
import json
import environ
from Accounts.models import Account
from Budget.models import BankAccount, MonthlySummary
import requests
from .forms import UpdateChangedTransactions
import random
from .plaid_integrations import plaid_get_Transactions, plaid_get_account_balance

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
            "redirect_uri": "https://www.prosperon-university.com/budget/oauth.html",

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
    account = Account.objects.filter(pk=request.user.pk)
    user_id = account.model.get_user_id(self=user)
    changed_transactions = account.model.get_changed_transactions(self=user)
    print(changed_transactions['user_accounts'])


    if request.POST.get('action') == 'post':
        print('this is accounts test')
        public = request.POST['public_token']

        url = 'https://development.plaid.com/item/public_token/exchange'

        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            "client_id": f"{CLIENT_ID}",
            "secret": f"{SECRET}",
            "public_token": f"{public}",

        }

        r = requests.post(url, headers=headers, json=data)
        print(r.json())

        access_token = r.json()['access_token']

        print(access_token)
        account_id = random.randint(100000000000, 999999990000)
        packaged = {"account_token": f"{access_token}", "id": f"{account_id}"}
        changed_transactions = changed_transactions['user_accounts'].append(packaged)
        changed_transactions.save()


    return render(request, 'Budget/oauth.html')



# Budget Dashboard
def budget_dashboard(request):
    user = request.user
    if user.is_active and user.has_budget == True:
        account = Account.objects.filter(pk=request.user.pk)
        user_id = account.model.get_user_id(self=user)
        changed_transactions = account.model.get_changed_transactions(self=user)
        bank_accounts = BankAccount.objects.filter(users_id=user_id)
        goals = Goal.objects.filter(users_id=user_id)

        print(bank_accounts)
        # receiving AJAX from changing a transaction category
        if request.POST.get('action') == 'post':
            public = request.POST
            print(public)




    # Getting transactions for account
    transactions = plaid_get_Transactions(CLIENT_ID, SECRET, 'access-development-d608958f-5ab7-402e-a8b8-0231a53a5ce5')
    print(transactions)

    # Getting account balances
    balance = plaid_get_account_balance(CLIENT_ID, SECRET, 'access-development-d608958f-5ab7-402e-a8b8-0231a53a5ce5')
    test_balance = (balance['accounts'][0]['balances']['available'])



    context = {
        'transaction_data': transactions,
        'test_balance': test_balance,
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
        bank_accounts = BankAccount.objects.filter(users_id=user_id)
        monthly_summary = MonthlySummary.objects.filter(users_id=user_id)[:1]
        monthly_summary = monthly_summary.get().all_transactions
        monthly_summary = json.dumps(monthly_summary)


        # Getting all accounts
        for account in bank_accounts:
            token = account.token
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






        context = {
            'transaction_data': transaction_data
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