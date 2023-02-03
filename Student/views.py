import random

from django.shortcuts import render, redirect
from .models import video
from Accounts.models import Account
from Student.models import Student, ModuleSummarie, AnytimeDecision, BudgetItemsUniversity, Apartment, Job, UniversityModule, CreditCard, BankAccount
from .forms import AddBudgetForm, NewModuleSummaryForm
import json
from django import template


register = template.Library()

@register.filter()
def to_int(value):
    return int(value)



# ------- UNIVERSITY MAIN VIEWS -----------

# University Dashboard
def dashboard(request):
    user = request.user


    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student_model = Student.objects.get(user_id_number=user_id)
        student_job_id = student_model.accepted_job

        first_name = student_model.first_name
        last_name = student_model.last_name
        profile_image = student_user.model.get_user_image(self=user)
        student_path = student_model.life_path['events']
        jobpicked = student_model.accepted_job
        student_progress = student_model.course_progress



        if student_model.job is None:
            jobTitle = ''
        else:
            jobTitle = student_model.job.title


        if profile_image:
            pass
        else:
            profile_image = ''
        age = student_model.age
        location = student_model.location
        total_points = student_model.total_points
        last_points = student_model.last_points_added
        anytime_dec = AnytimeDecision.objects.all()



        context = {
            'first_name': first_name,
            'last_name': last_name,
            'profile_image': profile_image,
            'age': age,
            'anytime_dec': anytime_dec,
            'student_path': student_path,
            'jobTitle': jobTitle,
            'location': location,
            'total_points': total_points,
            'last_points': last_points,
            'student_progress': student_progress
        }

        return render(request, 'Students/dashboard.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')


# Budget / Goals Page
def goals(request):

    return render(request, 'Students/budget/goals.html')

# Budget / Add Goals
def add_goals(request):

    return render(request, 'Students/budget/add_goal.html')




# Budget / Budget page
def budget(request):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student_model = Student.objects.get(user_id_number=user_id)
        user_university_budget_items = BudgetItemsUniversity.objects.filter(users_id=user_id)
        yearly_salary = student_model.yearly_salary
        monthly_salary = student_model.yearly_salary / 12
        monthly_salary = round(monthly_salary)






        for budget in user_university_budget_items:
            title = budget.title

            total_spent_in_category = 0
            for transact in budget.transactions['categoryTransactions']:
                price = int(transact['amount'])
                total_spent_in_category += price

            title = budget.title
            total = total_spent_in_category



        context = {
            'user_university_budget_items': user_university_budget_items,
            'yearly_salary': yearly_salary,
            'monthly_salary': monthly_salary

        }
        return render(request, 'Students/budget/budget.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')


# Budget / Add budget
def add_budget(request):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student_model = Student.objects.get(user_id_number=user_id)

        if request.method == 'POST':
            print(request.POST)
            form = AddBudgetForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.transactions = {"categoryTransactions": []}
                instance.budget_id = random.randint(100000000,90000000000)
                instance.users_id = user_id
                instance.save()
                return redirect('/university/budget/budget')
        else:
            form = AddBudgetForm(request.POST)


    context = {
        'form': form
    }
    return render(request, 'Students/budget/add_budget.html', context=context)

# Budget / transactions page
def transactions(request):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student = Student.objects.get(user_id_number=user_id)
        budget_categories = BudgetItemsUniversity.objects.filter(users_id=user_id)

        print('test3214')
        # Code for receiving transactions with ajax
        if request.POST.get('action') == 'post':
            public = request.POST
            transaction_category = public['test']
            transaction_id = public['the_id']

            amount = public['amount']
            print(amount)
            print(type(amount))
            amount = float(amount)
            print(type(amount))


            print(transaction_category)
            budget_category = BudgetItemsUniversity.objects.get(title=transaction_category)

            currentTransactions = budget_category.transactions['categoryTransactions']

            new_packaged_transaction =  {

                         "date":"2017-01-29",
                         "name":"Apple Store",
                         "amount": amount,
                         "category":[
                            "Shops",
                            "Computers and Electronics"
                         ],
                         "location":{
                            "lat":40.740352,
                            "lon":-74.001761,
                            "city":"San Francisco",
                            "region":"CA",
                            "address":"300 Post St",
                            "country":"US",
                            "postal_code":"94108",
                            "store_number":"1235"
                         },
                         "transaction_id": f"{transaction_id}",
                         "category_id":"19013000",

                      }

            currentTransactions.append(new_packaged_transaction)

            if budget_category.current_total:

                budget_category.current_total = int(budget_category.current_total) + amount
            else:
                budget_category.current_total = amount

            budget_category.save()


            print(amount)
            print(currentTransactions)

        transactions = student.all_transactions
        new_current_transactions = transactions['all_transactions']

        context = {
            'budget_categories': budget_categories,
            'new_current_transactions': new_current_transactions
        }
        return render(request, 'Students/budget/transactions.html', context=context)

# Universal Video Page
def universal_video(request, id):
    the_video = video.objects.get(id=id)
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        print(request.POST)
        if user.is_active:
            if request.method == 'POST':
                progress = request.POST['progress']
                next_btn = request.POST['next-button']
                student_model = Student.objects.get(user_id_number=user_id)
                print(student_model.course_progress)
                if student_model.course_progress < progress:
                    student_model.course_progress = progress
                    student_model.save()


                    return redirect(f'/{next_btn}')
                else:
                    return redirect(f'/{next_btn}')
            print(request.POST)


            context = {
                'video': the_video
            }
            return render(request, 'Students/uni-video.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')


# End of module summaries
def module_summaries(request, id, c):
    user = request.user
    if user.is_active and user.has_university == True:
        summary = ModuleSummarie.objects.get(user=user, module_url=id)
        summary_title = summary.module.module_title
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student = Student.objects.get(user_id_number=user_id)

        next_module = summary.module.next_life_event['nextEvent']
        print(next_module)

        print(next_module['title'])

        # Defining page type for buttons on front end
        page_type = c

        # Getting max points for doing module
        student_total_points = student.total_points
        modulePoints = UniversityModule.objects.get(module_id=id).points
        total_points = student_total_points + modulePoints
        student.last_points_added = modulePoints
        student.total_points = total_points
        student.save()



        # Generating unlocked anytime decisions
        unlocked_decisions = UniversityModule.objects.get(module_id=id).unlocked_decisions
        unlocked_decisions = json.loads(unlocked_decisions)
        all_unlocked_decisions = []
        all_unlocked_decision_ids = []

        # Cleaning unlocked anytime decisions and putting them into new list
        for i in unlocked_decisions:
            decision = AnytimeDecision.objects.get(decision_id=i)
            all_unlocked_decisions.append(decision)
            all_unlocked_decision_ids.append(decision.decision_id)


        # Checking to see if there are any unlocked anytime decisions
        unlocked = student.unlocked_anytime_decisions

        if unlocked is None:
            student.unlocked_anytime_decisions = all_unlocked_decision_ids
            student.save()
        else:
            pass


        # appending upcoming life event to timeline
        if c == '0':
            decisions = []
            for decision in student.life_path['events']:
                decisions.append(decision['title'])

            if next_module['title'] in decisions:
                pass
            else:
                student.life_path['events'][-1]['status'] = "completed"
                student.total_points = total_points
                student.life_path['events'].append(next_module)
                student.save()



        context = {
            'summary': summary,
            'summary_title': summary_title,
            'page_type': page_type,
            'anytime_dec': all_unlocked_decisions,
            'modulePoints': modulePoints,
            'total_points': total_points

        }
        return render(request, 'Students/module_summary.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')

# all anytime decisions
def anytime_decision_bank(request):
    anytime_decisions = AnytimeDecision.objects.all()

    context = {
        "anytime_decisions": anytime_decisions
    }
    return render(request, 'Students/all_anytime_decisions.html', context=context)

# Specific Anytime Decision
def anytime_decision(request, id):
    ad = AnytimeDecision.objects.get(pk=id)

    context = {
        'ad': ad
    }
    return render(request, 'Students/anytime-decision.html', context=context)


def anytime_decision_step2(request, id):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student = Student.objects.get(user_id_number=user_id)
        ad = AnytimeDecision.objects.get(decision_id=id)
        html_path = ad.step2_path
        print(html_path)
        apartments = Apartment.objects.all()
        credit_cards = CreditCard.objects.all()
        bank_accounts = BankAccount.objects.all()\

        student_job_location = str(student.job.job_city)
        student_current_location = str(student.location)




        # Grabbing request
        if request.method == 'POST':
            print('there was a request')
            print(request.POST)
            sent_form = request.POST
            full_life_path = student.life_path['events']

            # removed object
            upcoming_module = student.life_path['events'][-1]
            del full_life_path[-1]

            # Adding anytime Decision
            anytime = {
                "title": f"{ad.title}",
                "type": "Anytime Decision",
                "description": f"{ad.description}",

            }



            cost_now = sent_form['cost-now']
            monthly_cost = sent_form['cost-later']
            transaction_title = sent_form['transactiontitle']





            monthly_cost = monthly_cost.replace(',', '')
            monthly_cost = float(monthly_cost)
            print(type(monthly_cost))
            student_current_monthhly_expenses = student.total_monthly_expenses
            student.total_monthly_expenses = student_current_monthhly_expenses - monthly_cost





            student.save()




            if monthly_cost != '0':
                transaction_id = random.randint(1231456437657543635423452323452345242,9231456437657543635423452323452345242)

                new_packaged_transaction = {

                    "date": "2017-01-29",
                    "name": transaction_title,
                    "length": 12,
                    "amount": monthly_cost,
                    "category": [
                        "Payment",
                        "Computers and Electronics"
                    ],
                    "location": {
                        "lat": 40.740352,
                        "lon": -74.001761,
                        "city": "San Francisco",
                        "region": "CA",
                        "address": "300 Post St",
                        "country": "US",
                        "postal_code": "94108",
                        "store_number": "1235"
                    },
                    "transaction_id": f"{transaction_id}",
                    "category_id": "19013000",

                }

                student_montly_transactions = student.monthly_transactions['monthly_transactions']
                student_montly_transactions.append(new_packaged_transaction)
                student.monthly_transactions['monthly_transactions'] = student_montly_transactions


                current_all_transactions = student.all_transactions['all_transactions']
                print(current_all_transactions)
                current_all_transactions.append(new_packaged_transaction)
                print(current_all_transactions)

                student.save()






            full_life_path.append(anytime)
            full_life_path.append(upcoming_module)
            new = {"events": full_life_path}
            student.life_path = new
            ad_points = ad.points
            student.last_points_added = ad_points
            student.total_points = student.total_points + ad_points
            student.save()
            return redirect('/university/dashboard')




        context = {
            'ad': ad,
            'id': id,
            'apartments': apartments,
            'credit_cards': credit_cards,
            'bank_accounts': bank_accounts,
            'student': student,
            'student_job_location': student_job_location,
            'student_current_location': student_current_location

        }
        return render(request, f'Students/anytime-decisions/{html_path}', context=context)
    else:
        return render(request, 'MainWebsite/index.html')
