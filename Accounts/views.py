from django.shortcuts import render, redirect
from .forms import BudgetAccountRegistrationForm, StudentAccountRegistrationForm, AddStudentAccountForm
import random
import datetime
from django.contrib.auth import login as djlogin
from Student.models import Student
from django.contrib import auth

# Logout Page
def logout(request):
    auth.logout(request)

    return render(request, 'MainWebsite/index.html')

# Login for student
def login_student(request):
    return render(request, 'Accounts/login-student.html')


# Registration choice
def register_choice(request):
    return render(request, 'Accounts/registration-choice.html')


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
        print(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            created_user_id = random.randint(100000000000,999999990000)
            user.user_id = created_user_id
            user.has_university = True
            user.username = created_user_id
            user.set_password(user.password)
            user.last_login = datetime.datetime.now()
            user.save()
            djlogin(request, user, backend='django.contrib.auth.backends.ModelBackend')
            studentAccountForm = AddStudentAccountForm(request.POST, request.FILES)
            studentUser = studentAccountForm.save(commit=False)
            studentUser.user = request.user
            class_code = request.POST['class_code']
            studentUser.class_code = class_code
            studentUser.user_id_number = created_user_id
            studentUser.life_path = {"events": [
                    {
                        "title": "First Job",
                        "type": "Life Event",
                        "status": "not-started",
                        "imgurl": "../../media/moduleImages/first-job-img.jpg",
                        "description": "This Life Event walks you through getting your first job",
                        "summaryPage": "first_job",
                        "videoPageId": "1"
                    }
                ]
            }
            studentUser.student_email = request.user
            studentUser.total_points = 0
            studentUser.last_points_added = 0
            studentUser.total_monthly_expenses = 0
            studentUser.course_progress = 0
            studentUser.spender_type = '0'
            studentUser.all_transactions = {"all_transactions": []}
            studentUser.monthly_transactions = {"monthly_transactions": []}
            studentUser.spending_profile_monthly_payments = {"spending_profile_monthly_payments": []}
            studentUser.save()





            djlogin(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/university/onboarding/step1')

    else:
        form = BudgetAccountRegistrationForm(request.POST, request.FILES)

    context = {

        'form': form

    }
    return render(request, 'Accounts/register-student.html', context=context)