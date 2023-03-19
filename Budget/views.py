from django.shortcuts import render, redirect
from .models import Goal, BudgetItems, BudgetUsers
import json
import environ
from Accounts.models import Account
from Budget.models import BankAccount, MonthlySummary
import requests
from .forms import UpdateChangedTransactions, AddBudgetForm
import random
from .plaid_integrations import plaid_get_Transactions, plaid_get_account_balance
from .functions import package_transaction
import datetime as dt

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


def refresh(request):
    user = request.user
    if user.is_active and user.has_budget == True:
        account = Account.objects.filter(pk=request.user.pk)
        user_id = account.model.get_user_id(self=user)
        changed_transactions = account.model.get_changed_transactions(self=user)
        bank_accounts = BankAccount.objects.filter(users_id=user_id)
        budget_user = BudgetUsers.objects.get(users_id=user_id)

        # Getting account balances
        balance = plaid_get_account_balance(CLIENT_ID, SECRET, 'access-development-d608958f-5ab7-402e-a8b8-0231a53a5ce5')
        budget_user.checking_savings_total = float(balance['accounts'][0]['balances']['available'])
        budget_user.save()
        return redirect('/budget/dashboard')


    return render(request, 'Budget/dashboard.html')


# Budget Dashboard
def budget_dashboard(request):
    user = request.user
    if user.is_active and user.has_budget == True:
        account = Account.objects.filter(pk=request.user.pk)
        user_id = account.model.get_user_id(self=user)
        changed_transactions = account.model.get_changed_transactions(self=user)
        bank_accounts = BankAccount.objects.filter(users_id=user_id)
        budget_user = BudgetUsers.objects.get(users_id=user_id)

        # Basic information
        checking_and_savings_total = budget_user.checking_savings_total
        credit_avaliable = budget_user.credit_avaliable
        investments = budget_user.investments
        loans = budget_user.loans
        real_estate = budget_user.real_estate

        print(checking_and_savings_total)

        goals = Goal.objects.filter(users_id=user_id)
        current_date = dt.date.today()

        start_date = str(current_date).split("-")
        start_date[1] = '01'
        start_date = '-'.join(start_date)
        print(start_date)

        print(bank_accounts)
        # receiving AJAX from changing a transaction category
        if request.POST.get('action') == 'post':
            public = request.POST
            print(public)




        # Getting transactions for account
        transactions = plaid_get_Transactions(CLIENT_ID, SECRET, 'access-development-d608958f-5ab7-402e-a8b8-0231a53a5ce5', start_date, current_date)
        print(transactions)





        context = {
            'transaction_data': transactions,
            'checking_and_savings_total': checking_and_savings_total,
            'credit_avaliable': credit_avaliable,
            'investments': investments,
            'loans': loans,
            'real_estate': real_estate
        }

        return render(request, 'Budget/dashboard.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')

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
        budget_categories = BudgetItems.objects.filter(users_id=user_id)
        current_date = dt.date.today()

        start_date = str(current_date).split("-")
        start_date[1] = '01'
        start_date = '-'.join(start_date)
        print(start_date)

        print(current_date)

        transactions = plaid_get_Transactions(CLIENT_ID, SECRET, 'access-development-d608958f-5ab7-402e-a8b8-0231a53a5ce5', f'{start_date}', f'{current_date}')



        print(transactions[0])
        if request.POST.get('action') == 'post':
            print(request.POST)
            public = request.POST
            transaction_category = public['test']
            print(transaction_category)
            transaction_id = public['the_id']
            amount = public['amount']
            tran_title = public['tran_title']
            transaction_date = public['transaction_date']
            print(transaction_date)

            amount = float(amount)
            category1 = public['category1']
            category2 = public['category2']
            transaction_budget = public['budget']

            new_packaged_transaction = package_transaction(tran_title, transaction_budget, amount, category1, category2, transaction_id)


            print(transaction_budget)

            # Specific budget category
            budget_category = BudgetItems.objects.get(budget_id=transaction_budget, users_id=user_id)
            print('budget category: ', budget_category.title)

            all_budgets = BudgetItems.objects.filter(users_id=user_id)
            for budg in all_budgets:
                category_transactions = budg.transactions['categoryTransactions']
                # Checking to see if the transaction has been in any budgets
                if (transaction_budget == budg.budget_id):
                    category_transactions.append(new_packaged_transaction)
                    budget_category.transactions['categoryTransactions'] = category_transactions
                    budget_category.current_total = budget_category.current_total + amount
                    budget_category.save()
                    print('its saved')

        context = {
            'transaction_data': transactions,
            'budget_categories': budget_categories,

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
        budget_user = BudgetUsers.objects.get(users_id=user_id)

        average_income = budget_user.average_income
        print(all_budgets)


        context = {
            'all_budgets': all_budgets,
            'average_income': average_income,
        }

        return render(request, 'Budget/budget.html', context=context)

    else:
        return render(request, 'MainWebsite/index.html')


# Page for adding budget
def add_budget(request):
    user = request.user
    if user.is_active and user.has_budget == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        if request.method == 'POST':
            form = AddBudgetForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.transactions = {"categoryTransactions": []}
                instance.budget_id = random.randint(100000000, 90000000000)
                instance.users_id = user_id
                instance.current_total = 0
                instance.save()
                return redirect('/budget/dashboard')
        else:
            form = AddBudgetForm(request.POST)

        context = {
            'form': form
        }
        return render(request, 'Budget/add_budget.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')

# Page for viewing budget
def view_budget(request, id):
    user = request.user
    if user.is_active and user.has_budget == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        student_budget = BudgetItems.objects.get(budget_id=id)
        budget_categories = student_budget.CATAGORIES

        budget_purchases = student_budget.transactions

        if request.method == 'POST':
            post = request.POST
            print(request.POST)
            budget_name = post['budget-title']
            budget_max = post['Max-amount']
            budget_category = post['Category']
            print('changed budget')

            for categories in budget_categories:
                if categories[0] == budget_category:
                    num = categories[0]

            student_budget.title = budget_name
            student_budget.total_per_month = budget_max
            student_budget.category = num
            student_budget.save()

            return redirect('/budget/budget')

        context = {
            'student_budget': student_budget,
            'budget_categories': budget_categories,
            'budget_purchases': budget_purchases
        }
        return render(request, 'Budget/view_budget.html', context=context)

# Page for deleting budget
def delete_budget(request, id):
    user = request.user
    if user.is_active and user.has_budget == True:
        student_budget = BudgetItems.objects.get(budget_id=id)
        student_budget.delete()
        return redirect('/budget/budget')


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