from django.shortcuts import render, redirect
from Student.forms import UpdateProgressForm, NewModuleSummaryForm
from Student.models import Student, Major, UniversityModule, Subscription, MonthlyExpense
from Accounts.models import Account
import random



def budgeting_step1(request):
    user = request.user
    student_user = Account.objects.filter(pk=request.user.pk)
    user_id = student_user.model.get_user_id(self=user)
    student_model = Student.objects.get(user_id_number=user_id)
    spending_profile_type = student_model.spender_type

    # Checking users cradentials
    if user.is_active and user.has_university == True:
        subscriptions = Subscription.objects.all()
        monthly_expenses = MonthlyExpense.objects.all()
        monthly_expenses_ranges = monthly_expenses.model.RANGES

        # Handling subscription submissions with AJAX
        if request.POST.get('action') == 'post':
            newSubscription = request.POST
            print(newSubscription['type'])

            # Logic when form request is for a subscription
            if newSubscription['type'] == 'sub':
                companyName = newSubscription['companyName']
                subscriptionCost = newSubscription['subscriptionCost']
                transaction_id = random.randint(1231456437657543635423452323452345242, 9231456437657543635423452323452345242)

                new_packaged_transaction = {
                    "date": "2017-01-29",
                    "name": f"{companyName}",
                    "associated_budget": "none",
                    "amount": subscriptionCost,
                    "checked": "no",
                    "category": [
                        "Subscription",
                        "Subscription"
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

                # Adding subscription to new model
                currentMonthlyTransactions = student_model.monthly_transactions['monthly_transactions']
                allTransactions = student_model.all_transactions['all_transactions']


                total = float(student_model.total_monthly_expenses) - float(subscriptionCost)
                student_model.total_monthly_expenses = total


                allTransactions.append(new_packaged_transaction)
                currentMonthlyTransactions.append(new_packaged_transaction)

                student_model.save()


            # Logic when form request is for a monthly transaction
            elif newSubscription['type'] == 'mon':
                print('monthly')
                # getting data for monthly costs
                companyName = newSubscription['companyName']

                subscriptionCost = newSubscription['subscriptionCost']
                cleaned_subscription_cost = subscriptionCost.replace('$', '')
                cleaned_subscription_cost = (cleaned_subscription_cost.partition("-"))
                subscription_cost_low = int(cleaned_subscription_cost[0])
                subscription_cost_high = int(cleaned_subscription_cost[2])
                print(subscription_cost_low)
                print(subscription_cost_high)

                if spending_profile_type == '0':
                    low = subscription_cost_low + 50
                    high = subscription_cost_high
                    random_cost = random.randint(low, high)
                    print(random_cost, '- spender')

                elif spending_profile_type == '1':
                    low = subscription_cost_low + 25
                    high = subscription_cost_high - 25
                    random_cost = random.randint(low, high)
                    print(random_cost, '- planner')
                elif spending_profile_type == '2':
                    low = subscription_cost_low
                    high = subscription_cost_high - 50
                    random_cost = random.randint(low, high)
                    print(random_cost, '- frugal')
                else:
                    random_cost = 0



                print(random_cost)

                transaction_id = random.randint(1231456437657543635423452323452345242, 9231456437657543635423452323452345242)

                new_packaged_transaction = {
                    "date": "2017-01-29",
                    "name": f"{companyName}",
                    "associated_budget": "none",
                    "amount": random_cost,
                    "checked": "no",
                    "category": [
                        "Payment",
                        "Payment"
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

                # Adding subscription to new model
                currentMonthlyTransactions = student_model.monthly_transactions['monthly_transactions']
                allTransactions = student_model.all_transactions['all_transactions']

                total = float(student_model.total_monthly_expenses) - float(random_cost)
                student_model.total_monthly_expenses = total

                student_model.spending_profile_monthly_payments['spending_profile_monthly_payments'].append(new_packaged_transaction)

                allTransactions.append(new_packaged_transaction)
                currentMonthlyTransactions.append(new_packaged_transaction)

                student_model.save()


        if request.method == 'POST':

            if int(student_model.course_progress) < 15:


                student_model.course_progress = 15
                student_model.save()
                return redirect('/university/video/6')
            else:
                return redirect('/university/video/6')


        context = {
            'subscriptions': subscriptions,
            'monthly_expenses': monthly_expenses,
            'monthly_expenses_ranges': monthly_expenses_ranges
        }



        return render(request, 'Students/m2-budgeting/step1.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')


def budgeting_step2(request):
    user = request.user
    student_user = Account.objects.filter(pk=request.user.pk)
    user_id = student_user.model.get_user_id(self=user)
    student_model = Student.objects.get(user_id_number=user_id)
    spender_category = student_model.spender_type




    if user.is_active and user.has_university == True:
        if request.method == 'POST':
            progress = request.POST['progress']

            if student_model.course_progress < progress:

                if spender_category == '0':
                    spender_type = 'Spender'
                elif spender_category == '1':
                    spender_type = 'Planner'
                elif spender_category == '2':
                    spender_type = 'Frugal'
                else:
                    spender_type = ''

                module_summary_form = NewModuleSummaryForm(request.POST, request.FILES)
                newModule = module_summary_form.save(commit=False)
                newModule.user = request.user
                newModule.module_url = 'budgeting'
                newModule.module = UniversityModule.objects.get(module_title='Budgeting')
                newModule.users_id = user_id
                packaged = {"module_results":  [{"title":  "Budgeting Unlocked"}, {"title":  "Simulation Unlocked"}, {"title": f"You are a {spender_type}"}]}
                newModule.module_results = packaged
                newModule.save()
                print('sent234')





                student_model.course_progress = progress
                student_model.save()

                return redirect('/university/budget/transactions')
            else:
                return redirect('/university/budget/transactions')

        return render(request, 'Students/m2-budgeting/step2.html')
    else:
        return render(request, 'MainWebsite/index.html')


def budgeting_step3(request):
    user = request.user
    student_user = Account.objects.filter(pk=request.user.pk)
    user_id = student_user.model.get_user_id(self=user)
    student_model = Student.objects.get(user_id_number=user_id)
    first_name = student_model.first_name
    last_name = student_model.last_name


    if user.is_active and user.has_university == True:
        if request.method == 'POST':
            progress = request.POST['progress']
            if student_model.course_progress < progress:
                student_model.course_progress = progress
                student_model.save()
                return redirect('/university/onboarding/step3')
            else:
                return redirect('/university/onboarding/step3')

        context = {
            'first_name': first_name,
            'last_name': last_name,
        }


        return render(request, 'Students/m2-budgeting/step3.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')
