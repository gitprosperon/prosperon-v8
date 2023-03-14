import random

from django.shortcuts import render, redirect
from .models import video
from Accounts.models import Account
from Student.models import Student, ModuleSummarie, AnytimeDecision, BudgetItemsUniversity, Apartment, Job, UniversityModule, CreditCard, BankAccount, Subscription, MonthlyExpense
from Student.models import Property, Scenario
from .forms import AddBudgetForm, NewModuleSummaryForm
import json
from django import template
import datetime


register = template.Library()

@register.filter()
def to_int(value):
    return int(value)


def compounding_growth(principal, interest_rate, time, monthlyIncome, MonthlyExpenses):
    # Calculate the compound interest
    compound_interest = (principal + ((monthlyIncome + MonthlyExpenses) * time) * ((1 + ( (interest_rate / 100) / 12 )) ** (time / 12)))
    return compound_interest



# ------- UNIVERSITY MAIN VIEWS -----------

# University Dashboard
def dashboard(request):
    user = request.user
    print(user)
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student_model = Student.objects.get(user_id_number=user_id)
        student_job_id = student_model.accepted_job

        # Basic information
        first_name = student_model.first_name
        last_name = student_model.last_name
        profile_image = student_user.model.get_user_image(self=user)
        student_path = student_model.life_path['events']
        jobpicked = student_model.accepted_job
        student_progress = int(student_model.course_progress)
        current_year = student_model.current_year
        investing_activated = student_model.investing_activated
        monthly_spending_habits = student_model.spending_profile_monthly_payments['spending_profile_monthly_payments']
        spending_profile_ranges = MonthlyExpense.RANGES
        monthly_expenses = MonthlyExpense.objects.all()
        current_year_calculated = int(student_model.current_month) // 12
        living_situation = student_model.living_situation
        apartment = student_model.apartments
        properties = student_model.properties['properties']
        avaliable_scenarios = list(student_model.avaliable_scenarios.split(','))
        scenario_choice = random.choice(avaliable_scenarios)
        the_scenario = Scenario.objects.get(scenario_id=scenario_choice)
        scenario_display = student_model.scenario_display
        todays_date = datetime.date.today()


        # Checking to see if there is a job
        if student_model.job is None:
            jobTitle = ''
        else:
            jobTitle = student_model.job.title

        # Checking to see if there is a profile image
        if profile_image:
            pass
        else:
            profile_image = ''
        age = student_model.age
        location = student_model.location
        total_points = student_model.total_points
        last_points = student_model.last_points_added
        anytime_dec = AnytimeDecision.objects.all()

        # Filtering for anytime decisions
        if student_model.unlocked_anytime_decisions != None:
            # Code for cleaning unlocked anytime decision list
            user_unlocked_anytimeDecisions = student_model.unlocked_anytime_decisions.replace("'", "")
            user_unlocked_anytimeDecisions = user_unlocked_anytimeDecisions.replace("[", "")
            user_unlocked_anytimeDecisions = user_unlocked_anytimeDecisions.replace("]", "")
            user_unlocked_anytimeDecisions = user_unlocked_anytimeDecisions.split(", ")
            user_monthly_surplus = (student_model.yearly_salary / 12) + (student_model.total_monthly_expenses)
            print(user_monthly_surplus)

            decision_list = []
            for i in user_unlocked_anytimeDecisions:
                if i not in student_model.completedAnytimeDecisions:
                    print(i)
                    decision = AnytimeDecision.objects.get(decision_id=i)
                    decision_list.append(decision)
        else:
            decision_list = ''

        # For passing in monthly net income list
        monthlyList = student_model.net_worth_monthly_list['net_income_monthly_list']

        # data for more information section
        monthly_transactions = student_model.monthly_transactions['monthly_transactions']
        subscriptions = Subscription.objects.all()
        student_life_path = student_model.life_path['events']

        try:
            job = Job.objects.get(job_id=jobpicked)
        except:
            job = ''

        salary = student_model.yearly_salary


        context = {
            'first_name': first_name,
            'last_name': last_name,
            'profile_image': profile_image,
            'age': age,
            'anytime_dec': decision_list,
            'student_path': student_path,
            'jobTitle': jobTitle,
            'location': location,
            'total_points': total_points,
            'last_points': last_points,
            'student_progress': student_progress,
            'monthlyList': monthlyList,
            'current_year': current_year,
            'monthly_transactions': monthly_transactions,
            'subscriptions': subscriptions,
            'student_life_path': student_life_path,
            'investing_activated': investing_activated,
            'monthly_spending_habits': monthly_spending_habits,
            'spending_profile_ranges': spending_profile_ranges,
            'living_situation': living_situation,
            'jobpicked': job,
            'salary': salary,
            'apartment': apartment,
            'properties': properties,
            'current_year_calculated': current_year_calculated,
            'monthly_expenses': monthly_expenses,
            'the_scenario': the_scenario,
            'scenario_display': scenario_display,
            'todays_date': todays_date

        }

        return render(request, 'Students/dashboard.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')


# Link to simulate time
def simulate(request, months):
    user = request.user

    # Seeing if user is active
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student = Student.objects.get(user_id_number=user_id)
        student_current_month = student.current_month
        investing_activated = student.investing_activated


        # Student financial data
        student_net_worth = student.current_net_worth
        student_monthlyIncome = int(student.yearly_salary / 12)
        monthlyExpenses = student.total_monthly_expenses
        net_worth_list = student.net_worth_monthly_list['net_income_monthly_list']
        mutule_fund_rate = 5.12
        surplus = student_monthlyIncome + monthlyExpenses
        print(surplus)

        # Calculating net worth each month
        index = 0
        net_worth = student_net_worth
        while index < int(months):
            index += 1
            netWorth = compounding_growth(net_worth, mutule_fund_rate, index, student_monthlyIncome, monthlyExpenses)
            net_worth_list.append({"net_worth": f"{netWorth}"})

        total_current_net_worth = compounding_growth(net_worth, mutule_fund_rate, int(months), student_monthlyIncome, monthlyExpenses)
        student.current_net_worth = total_current_net_worth
        student.net_worth_monthly_list['net_income_monthly_list'] = net_worth_list
        student.save()

        # adding months to total number of months
        totalMonths = student.total_months_completed
        total = int(months) + totalMonths
        student.total_months_completed = total

        # Creating current year
        student_current_year = student.current_year
        test = round(int(months) / 12)
        student.current_year = test + int(student_current_year)

        # Changing students age
        current_year = test + int(student_current_year)
        test4 = current_year - int(student.birth_year)
        student.age = test4

        student.save()

        return redirect('/university/dashboard')

    return render(request, 'Students/simulate.html')


# Budget / Dashboard
def budgetDashboard(request):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student_model = Student.objects.get(user_id_number=user_id)

        # Basic user information
        current_net_worth = student_model.current_net_worth
        investing_activated = student_model.investing_activated
        current_year_calculated = int(student_model.current_month) // 12
        monthlyList = student_model.net_worth_monthly_list['net_income_monthly_list']
        age = student_model.age
        transactions = student_model.all_transactions
        all_current_transactions = transactions['all_transactions']


        context = {
            'current_net_worth': current_net_worth,
            'investing_activated': investing_activated,
            'current_year_calculated': current_year_calculated,
            'monthlyList': monthlyList,
            'age': age,
            'all_current_transactions': all_current_transactions[:3]

        }
        return render(request, 'Students/budget/dashboard.html', context=context)
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
                instance.budget_id = random.randint(100000000, 90000000000)
                instance.users_id = user_id
                instance.current_total = 0
                instance.save()
                return redirect('/university/budget/budget')
        else:
            form = AddBudgetForm(request.POST)


    context = {
        'form': form
    }
    return render(request, 'Students/budget/add_budget.html', context=context)

# Budget / View Budget
def view_budget(request, id):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        student_budget = BudgetItemsUniversity.objects.get(budget_id=id)
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

            return redirect('/university/budget/budget')




        context = {
            'student_budget': student_budget,
            'budget_categories': budget_categories,
            'budget_purchases': budget_purchases
        }
        return render(request, 'Students/budget/view_budget.html', context=context)


# Code for deleting budget
def delete_budget(request, id):
    user = request.user
    if user.is_active and user.has_university == True:
        student_budget = BudgetItemsUniversity.objects.get(budget_id=id)
        student_budget.delete()
        return redirect('/university/budget/budget')


# Budget / transactions page
def transactions(request):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student = Student.objects.get(user_id_number=user_id)
        budget_categories = BudgetItemsUniversity.objects.filter(users_id=user_id)
        current_year = student.current_year

        # Code for receiving transactions with ajax
        if request.POST.get('action') == 'post':
            print(request.POST)
            public = request.POST
            transaction_category = public['test']
            print(transaction_category)
            transaction_id = public['the_id']
            amount = public['amount']
            tran_title = public['tran_title']

            amount = float(amount)
            category1 = public['category1']
            category2 = public['category2']
            transaction_budget = public['budget']
            print('')
            print('')
            print('')

            print(transaction_budget)


            # getting the budgeting category objext in database
            budget_category = BudgetItemsUniversity.objects.get(budget_id=transaction_budget)

            # A users current changed transactions json list
            currentTransactions = budget_category.transactions['categoryTransactions']
            all_transactions = student.all_transactions['all_transactions']

            for transaction in all_transactions:
                if transaction['transaction_id'] == transaction_id:

                    print('they are eqyal')
                    transaction['checked'] = 'yes'
                    transaction['associated_budget'] = f"{transaction_category}"
                    print(transaction)
                    student.save()

            print(len(currentTransactions))
            # Checking to see if any transactions exist
            if len(currentTransactions) == 0:
                new_packaged_transaction = {
                    "date": "2017-01-29",
                    "name": f"{tran_title}",
                    "associated_budget": f"{transaction_category}",
                    "amount": amount,
                    "checked": "yes",
                    "category": [
                        f"{category1}",
                        f"{category2}"
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
                currentTransactions.append(new_packaged_transaction)

                # Checking to  see if there is a current total for the monthly spend
                if budget_category.current_total:
                    budget_category.current_total = int(budget_category.current_total) + amount
                else:
                    budget_category.current_total = amount
                budget_category.save()

            else:
                print('curr tran')

                # Running logic for either editing or creating new
                for transact in currentTransactions:
                    print(transact)
                    if transaction_id == transact['transaction_id']:
                        print('Now we are editing current one')
                        print(transact['associated_budget'])

                        transact['checked'] = 'yes'
                        transact['associated_budget'] = f"{transaction_category}"
                        transact['category'][0] = category1
                        budget_category.save()
                    else:
                        print('New transaction to sent and packaged to budget')

                        # Packaging sent transaction
                        new_packaged_transaction =  {
                                     "date":"2017-01-29",
                                     "name": f"{tran_title}",
                                     "associated_budget": f"{transaction_category}",
                                     "amount": amount,
                                     "checked" : "yes",
                                     "category":[
                                        f"{category1}",
                                        f"{category2}"
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
                                     "category_id": "19013000",
                                  }
                        currentTransactions.append(new_packaged_transaction)

                        # Checking to  see if there is a current total for the monthly spend
                        if budget_category.current_total:
                            budget_category.current_total = int(budget_category.current_total) + amount
                        else:
                            budget_category.current_total = amount
                        budget_category.save()


        all_budgets = BudgetItemsUniversity.objects.filter(users_id=user_id)
        transactions = student.all_transactions
        all_current_transactions = transactions['all_transactions']

        balance = student.current_net_worth

        context = {
            'budget_categories': budget_categories,
            'new_current_transactions': all_current_transactions,
            'all_budgets': all_budgets,
            'balance': balance,
            'current_year': current_year


        }
        return render(request, 'Students/budget/transactions.html', context=context)


# Budget / accounts
def accounts(request):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student = Student.objects.get(user_id_number=user_id)
        budget_categories = BudgetItemsUniversity.objects.filter(users_id=user_id)
        current_year = student.current_year
        student_accounts = student.accounts['accounts']
        net_worth = student.current_net_worth

        # Calculating real estate value
        housing = student.properties['properties']

        if housing == []:
            total_real_estate_value = 0
        else:
            total_real_estate_value = 0
            for prop in housing:
                cost = int(prop['costNow'])
                total_real_estate_value += cost
                print(total_real_estate_value)


        context = {
            'student_accounts': student_accounts,
            'net_worth': net_worth,
            'total_real_estate_value': total_real_estate_value

        }
        return render(request, 'Students/budget/accounts.html', context=context)


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


# Review Video Page
def review_video(request, id, redirect_page, link_type):
    the_video = video.objects.get(id=id)
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        print(request.POST)
        if user.is_active:


            context = {
                'video': the_video,
                'redirect_page': redirect_page,
                'link_type': link_type
            }
            return render(request, 'Students/review_video.html', context=context)
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
        current_year = student.current_year
        student_month = student.current_month

        print('current year', current_year)
        module_results = summary.module_results

        # Getting next module
        next_module = summary.module.next_life_event['nextEvent']

        # Defining page type for buttons on front end
        page_type = c

        # Getting max points for doing module
        student_total_points = student.total_points
        modulePoints = UniversityModule.objects.get(module_id=id).points
        total_points = student_total_points + modulePoints
        student.last_points_added = modulePoints
        student.total_points = total_points
        student.save()

        # Code for getting module videos
        current_module = UniversityModule.objects.get(module_id=id)
        module_back_btn = current_module.back_btn
        current_videos = current_module.videos['videos']


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
            # cleaning unlocked from database
            unlocked = student.unlocked_anytime_decisions.replace("'", '').replace("[", "").replace("]", "").split(", ")
            for i in all_unlocked_decision_ids:
                if i in unlocked:
                    pass
                else:
                    unlocked.append(i)
                    student.unlocked_anytime_decisions = unlocked
                    student.save()

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
            'total_points': total_points,
            'current_videos': current_videos,
            'c': c,
            'current_year': current_year,
            'module_results': module_results['module_results'],
            'student_month': student_month,
            'module_back_btn': module_back_btn


        }
        return render(request, 'Students/module_summary.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')


# all anytime decisions
def anytime_decision_bank(request):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student = Student.objects.get(user_id_number=user_id)

        # Code for cleaning unlocked anytime decision list
        user_unlocked_anytimeDecisions = student.unlocked_anytime_decisions.replace("'", "")
        user_unlocked_anytimeDecisions = user_unlocked_anytimeDecisions.replace("[", "")
        user_unlocked_anytimeDecisions = user_unlocked_anytimeDecisions.replace("]", "")
        user_unlocked_anytimeDecisions = user_unlocked_anytimeDecisions.split(", ")
        user_monthly_surplus = (student.yearly_salary / 12 ) + (student.total_monthly_expenses)
        print(user_monthly_surplus)

        decision_list = []
        for i in user_unlocked_anytimeDecisions:
            decision = AnytimeDecision.objects.get(decision_id=i)
            decision_list.append(decision)





        context = {
            "anytime_decisions": decision_list
        }
        return render(request, 'Students/all_anytime_decisions.html', context=context)


# Specific Anytime Decision
def anytime_decision(request, id):
    ad = AnytimeDecision.objects.get(pk=id)

    context = {
        'ad': ad
    }
    return render(request, 'Students/anytime-decision.html', context=context)


# The second step for the anytime decisions
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
        properties = Property.objects.all()
        credit_cards = CreditCard.objects.all()
        bank_accounts = BankAccount.objects.all()

        student_job_location = str(student.job.job_city)
        student_current_location = str(student.location)
        student_current_net_worth = student.current_net_worth
        student_current_month = student.current_month




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

            # Checking to see if decision has to do with location
            if ad.title == "Move Out":
                student.living_situation = 'I Rent'
                student.save()
            if ad.title == "Buy a Property":
                print('it is own')


            # creating variables from form
            cost_now = sent_form['cost-now']
            monthly_cost = sent_form['cost-later']
            transaction_title = sent_form['transactiontitle']
            student.current_net_worth = student.current_net_worth - int(cost_now)



            # Cleaning and doing logic on monthly expenses
            monthly_cost = monthly_cost.replace(',', '')
            monthly_cost = float(monthly_cost)
            print(type(monthly_cost))
            student_current_monthhly_expenses = student.total_monthly_expenses
            student.total_monthly_expenses = student_current_monthhly_expenses - monthly_cost

            student.save()


            # Only running if it has a monthly cost that isn't 0
            if monthly_cost != '0':
                transaction_id = random.randint(1231456437657543635423452323452345242, 9231456437657543635423452323452345242)

                new_packaged_transaction = {
                    "date": "2017-01-29",
                    "name": transaction_title,
                    "checked": "no",
                    "associated_budget": "none",
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

                # Appending monthly transaction to monthly transaction list
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
            'student_current_location': student_current_location,
            'student_current_net_worth': student_current_net_worth,
            'properties': properties,
            'student_current_month': student_current_month

        }
        return render(request, f'Students/anytime-decisions/{html_path}', context=context)
    else:
        return render(request, 'MainWebsite/index.html')


# Pilot survey qualtrix page
def pilot_survey(request):
    return render(request, 'Students/pilot_survey.html')








