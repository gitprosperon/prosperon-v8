from django.shortcuts import render, redirect
from .forms import BudgetAccountRegistrationForm, StudentAccountRegistrationForm
import random
import datetime
from django.contrib.auth import login as djlogin
from Student.models import Student




# Create your views here.
def register_budget_account(request):
    if request.method == "POST":
        form = BudgetAccountRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            created_user_id = random.randint(100000000000,999999990000)
            user.user_id = created_user_id
            user.has_budget = True
            user.username = created_user_id
            user.set_password(user.password)
            user.last_login = datetime.datetime.now()
            user.save()
            djlogin(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/budget/accounts')

    else:
        form = BudgetAccountRegistrationForm(request.POST, request.FILES)


    context = {
        'form': form
    }

    return render(request, 'Accounts/register-budget-account.html', context=context)



def register_student_account(request):
    if request.method == 'POST':
        form = StudentAccountRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            created_user_id = random.randint(100000000000,999999990000)
            user.user_id = created_user_id
            user.has_university = True
            user.username = created_user_id
            user.last_login = datetime.datetime.now()
            user.save()

            test = Student.objects.create()
            test.user_id = created_user_id
            test.user = request.user
            test.save()


            djlogin(request, user, backend='django.contrib.auth.backends.ModelBackend')