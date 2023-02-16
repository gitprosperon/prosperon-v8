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
    print('trying to add a property')

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
            student_monthly_expenses = student_model.total_monthly_expenses - int(float(monthly_rent))
            student_model.total_monthly_expenses = student_monthly_expenses

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

            # Adding to life path tree
            full_life_path = student_model.life_path['events']

            # removed object
            upcoming_module = student_model.life_path['events'][-1]
            del full_life_path[-1]

            # Adding anytime Decision
            anytime = {
                "title": "Buy a House",
                "type": "Anytime Decision",
                "description": "Learn about buying a house and do it!",
            }

            full_life_path.append(anytime)
            full_life_path.append(upcoming_module)
            new = {"events": full_life_path}
            student_model.life_path = new
            student_model.living_situation = "I Own"

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


# Path for adding properties
def add_rental(request):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student_model = Student.objects.get(user_id_number=user_id)
        student_net_worth = student_model.current_net_worth
        student_properties = student_model.properties['properties']
        current_months_completed = student_model.total_months_completed
        print(request.POST)

        # Basic information
        post = request.POST
        property_title = post['title']
        property_type = post['type']
        the_address = post['the_address']
        costNow = post['costNow']
        city = post['city']
        monthly_rent = (post['monthly_rent']).replace(",", "")
        month_purchased = post['current_month']
        bed = post['bed']
        bath = post['bath']
        property_id = random.randint(100000000, 999999999999)

        # Changing students financials based on cost
        student_net_worth -= round(float(costNow))
        student_model.current_net_worth = student_net_worth
        student_monthly_expenses = student_model.total_monthly_expenses - int(float(monthly_rent))
        student_model.total_monthly_expenses = student_monthly_expenses

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


        # Adding to life path tree
        full_life_path = student_model.life_path['events']

        # removed object
        upcoming_module = student_model.life_path['events'][-1]
        del full_life_path[-1]

        # Adding anytime Decision
        anytime = {
            "title": "Move Out",
            "type": "Anytime Decision",
            "description": "In this module, users will evaluate the benefits of staying home versus the benefits of mo",
        }
        full_life_path.append(anytime)
        full_life_path.append(upcoming_module)
        new = {"events": full_life_path}
        student_model.life_path = new
        student_model.save()

        # Changing living situation status
        the_apartnment = Apartment.objects.get(address=the_address)
        student_model.apartments = the_apartnment
        student_model.living_situation = "I Rent"
        student_model.save()

        # Adding transaction amount
        transaction_id = random.randint(1231456437657543635423452323452345242, 9231456437657543635423452323452345242)
        new_packaged_transaction = {
            "date": "2017-01-29",
            "name": property_title,
            "checked": "no",
            "associated_budget": "none",
            "amount": monthly_rent,
            "category": [
                "Payment",
                "Rent Payment"
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
        student_montly_transactions = student_model.monthly_transactions['monthly_transactions']
        student_montly_transactions.append(new_packaged_transaction)
        student_model.monthly_transactions['monthly_transactions'] = student_montly_transactions
        current_all_transactions = student_model.all_transactions['all_transactions']
        print(current_all_transactions)
        current_all_transactions.append(new_packaged_transaction)
        print(current_all_transactions)
        student_model.save()






        return redirect('/university/dashboard')


# Path for removing rental property
def remove_rental(request):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student_model = Student.objects.get(user_id_number=user_id)
        student_net_worth = student_model.current_net_worth
        student_properties = student_model.properties
        current_months_completed = student_model.total_months_completed

        months_simulated = 0
        cleaned_months = 12 - (current_months_completed - ((current_months_completed // 12) * 12))

        # Getting ajax request
        if request.POST.get('action') == 'post':
            print('remove rental')
            post = request.POST
            property_id = post['property_id']
            monthly_cost = post['monthly_cost']

            for prop in student_properties['properties']:
                if prop['property_id'] == property_id:
                    print('they are equal ')
                    student_properties['properties'].remove(prop)
                    student_model.properties = student_properties
                    student_model.save()

            return redirect('/university/dashboard')


def add_account(request):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student_model = Student.objects.get(user_id_number=user_id)
        accounts = student_model.accounts['accounts']



        # Getting ajax request
        if request.POST.get('action') == 'post':
            print('add account')
            print(request.POST)
            post = request.POST
            cardType = post['cardType']
            bankName = post['bankName']
            image = post['image']
            apy = post['apy']
            yearlyFee = post['yearlyFee']
            atmFee = post['atmFee']
            description = post['description']
            bankFeature1 = post['bankFeature1']
            bankFeature2 = post['bankFeature2']
            bankFeature3 = post['bankFeature3']
            bankFeature4 = post['bankFeature4']

            if accounts == []:

                packaged_bank = {
                    'cardType': cardType,
                    'bankName': bankName,
                    'image': image,
                    'apy': apy,
                    'yearlyFee': yearlyFee,
                    'atmFee': atmFee,
                    'description': description,
                    'bankFeature1': bankFeature1,
                    'bankFeature2': bankFeature2,
                    'bankFeature3': bankFeature3,
                    'bankFeature4': bankFeature4

                }

                # Adding to life path tree
                full_life_path = student_model.life_path['events']

                # removed object
                upcoming_module = student_model.life_path['events'][-1]
                del full_life_path[-1]

                # Adding anytime Decision
                if cardType == 'CreditCard':
                    card_type = 'Credit Card'
                elif cardType == 'BankAccount':
                    card_type = 'Bank'


                anytime = {
                    "title": f"Open a {card_type} Account",
                    "type": "Anytime Decision",
                    "description": f"Learn about opening a {card_type} account and how to find the best bank account for you",
                }

                full_life_path.append(anytime)
                full_life_path.append(upcoming_module)
                new = {"events": full_life_path}
                student_model.life_path = new
                student_model.living_situation = "I Own"

                student_model.save()

                accounts.append(packaged_bank)
                student_model.accounts['accounts'] = accounts
                student_model.save()

            else:

                if bankName in accounts:
                    pass
                else:
                    print('we can add a new one now')

                    packaged_bank = {
                        'cardType': cardType,
                        'bankName': bankName,
                        'image': image,
                        'apy': apy,
                        'yearlyFee': yearlyFee,
                        'atmFee': atmFee,
                        'description': description,
                        'bankFeature1': bankFeature1,
                        'bankFeature2': bankFeature2,
                        'bankFeature3': bankFeature3,
                        'bankFeature4': bankFeature4

                    }

                    accounts.append(packaged_bank)
                    student_model.accounts['accounts'] = accounts
                    student_model.save()

                    # Adding to life path tree
                    full_life_path = student_model.life_path['events']

                    # removed object
                    upcoming_module = student_model.life_path['events'][-1]
                    del full_life_path[-1]

                    # Adding anytime Decision
                    if cardType == 'CreditCard':
                        card_type = 'Credit Card'
                    elif cardType == 'BankAccount':
                        card_type = 'Bank'

                    anytime = {
                        "title": f"Open a {card_type} Account",
                        "type": "Anytime Decision",
                        "description": f"Learn about opening a {card_type} account and how to find the best bank account for you",
                    }

                    full_life_path.append(anytime)
                    full_life_path.append(upcoming_module)
                    new = {"events": full_life_path}
                    student_model.life_path = new
                    student_model.living_situation = "I Own"

                    student_model.save()



            return redirect('/university/dashboard')


def anytime_decision_handeler(request, id):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student_model = Student.objects.get(user_id_number=user_id)
        ad = AnytimeDecision.objects.get(decision_id=id)

        # Adding points for anytime decision
        ad_points = ad.points
        student_model.last_points_added = ad.points
        print(student_model.last_points_added)

        student_model.save()
        student_model.total_points = student_model.total_points + ad_points
        print(student_model.total_points)
        student_model.save()

        print('anutome saved')







        print('we are handeling the anytime decision')

        return redirect('/university/dashboard')


    else:
        return render(request, 'MainWebsite/index.html')