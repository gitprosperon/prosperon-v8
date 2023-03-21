from django.shortcuts import render, redirect
import environ
from Accounts.models import Account
import requests
import random

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

    return render(request, 'Budget/add_account.html')


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


def refresh(request):
    user = request.user
    return redirect('/budget/dashboard')



# Budget Dashboard
def budget_dashboard(request):
    return render(request, 'Budget/dashboard.html')


# Goals page
def goals(request):
    user = request.user
    return render(request, 'Budget/Goals/goals.html')


# Page to add goals
def add_goals(request):
    user = request.user

    return render(request, 'Budget/Goals/add_goal.html')



# View individual goal
def view_goal(request, id):
    user = request.user
    return render(request, 'Budget/Goals/view_goal.html')


# Transactions page
def transactions(request):
    user = request.user
    return render(request, 'Budget/transactions.html')



# budget page
def budget(request):
    user = request.user
    return render(request, 'Budget/budget.html')


# Page for adding budget
def add_budget(request):
    user = request.user
    return render(request, 'Budget/add_budget.html')


# Page for viewing budget
def view_budget(request, id):
    user = request.user

    return render(request, 'Budget/view_budget.html')

# Page for deleting budget
def delete_budget(request, id):
    user = request.user

    return redirect('/budget/budget')


# accounts page
def accounts(request):
    user = request.user
    if user.is_active and user.has_budget == True:

        return render(request, 'Budget/accounts.html')


# notifications page
def notifications(request):
    user = request.user
    return render(request, 'Budget/notifications.html')