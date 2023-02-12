from django.shortcuts import render, redirect
from Student.models import Student, ModuleSummarie, AnytimeDecision, BudgetItemsUniversity, Apartment, Job, UniversityModule, CreditCard, BankAccount, Subscription
from Student.models import Property
from Accounts.models import Account
import random


# Path for removing subscriptions
def remove_subscriptions(request):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student_model = Student.objects.get(user_id_number=user_id)
        monthly_transactions = student_model.monthly_transactions['monthly_transactions']

        if request.POST.get('action') == 'post':
            print(request.POST)
            post = request.POST
            transaction_id = post['transaction_id']
            transaction_price = post['monthly_price']

            # Iterating through all monthly transactions to check if id matches
            for transaction in monthly_transactions:
                if transaction_id == transaction['transaction_id']:
                    print('they are equal')
                    monthly_transactions.remove(transaction)
            new_monthly_price = int(round(float(transaction_price))) + student_model.total_monthly_expenses
            student_model.total_monthly_expenses = new_monthly_price
            student_model.monthly_transactions['monthly_transactions'] = monthly_transactions
            student_model.save()

        return redirect('/university/dashboard')


    else:
        return render(request, 'MainWebsite/index.html')

# For updating spending habit
def update_spending_habit(request):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student_model = Student.objects.get(user_id_number=user_id)
        student_spending_habits = student_model.spending_profile_monthly_payments['spending_profile_monthly_payments']

        if request.POST.get('action') == 'post':
            print(request.POST)
            transaction_id = request.POST['transaction_id']
            new_range = request.POST['new_range']
            new_range_cleaned = new_range.replace("$", "").partition("-")
            print(new_range_cleaned)
            low_value = new_range_cleaned[0]
            high_value = new_range_cleaned[2]


    else:
        return render(request, 'MainWebsite/index.html')



# Path for adding properties
def add_property(request):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student_model = Student.objects.get(user_id_number=user_id)
        student_net_worth = student_model.current_net_worth
        print(request.POST)


        # Getting ajax request
        if request.POST.get('action') == 'post':
            post = request.POST
            property_title = post['title']
            property_type = post['type']
            the_address = post['the_address']
            costNow = post['costNow']
            city = post['city']
            monthly_rent = post['monthly_rent']
            month_purchased = post['current_month']
            bed = post['bed']
            bath = post['bath']
            property_id = random.randint(100000000, 999999999999)

            # Changing students financials based on cost
            student_net_worth -= round(float(costNow))
            student_model.current_net_worth = student_net_worth



            # Packaging new property
            new_property = {
                "title": f"{property_title}",
                "property_type": f"{property_type}",
                "address": f"{the_address}",
                "costNow": f"{costNow}",
                "city": f"{city}",
                "monthly_rent": f"{monthly_rent}",
                "bed": f"{bed}",
                "bath": f"{bath}",
                "property_id": f"{property_id}",
                "month_purchased": f"{month_purchased}"
            }

            student_model.properties['properties'].append(new_property)
            print(student_model.properties)
            student_model.save()

            return redirect('/university/dashboard')

# Path for adding properties
def sell_property(request):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student_model = Student.objects.get(user_id_number=user_id)
        student_net_worth = student_model.current_net_worth
        student_properties = student_model.properties['properties']
        current_months_completed = student_model.total_months_completed



        # Getting ajax request
        if request.POST.get('action') == 'post':
            print("sell property")
            post = request.POST
            print(request.POST)

            month_purchased = post['month_purchased']

            initial_cost = post['initial_cost']
            monthly_cost = post['monthly_cost']
            property_id = post['property_id']
            num_months = current_months_completed - int(month_purchased)
            num_years = num_months // 12
            answer = round(float(initial_cost) * (1 + .051 / num_years) ** (num_years))

            for prop in student_properties:
                if prop['property_id'] == property_id:
                    new_monthly_expenses = student_model.total_monthly_expenses + int(float(monthly_cost))
                    student_model.total_monthly_expenses = new_monthly_expenses
                    new_net_worth = student_net_worth + answer
                    student_model.current_net_worth = new_net_worth
                    student_properties.remove(prop)
                    student_model.save()



        return redirect('/university/dashboard')