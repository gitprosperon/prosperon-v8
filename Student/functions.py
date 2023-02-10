from django.shortcuts import render, redirect
from Student.models import Student, ModuleSummarie, AnytimeDecision, BudgetItemsUniversity, Apartment, Job, UniversityModule, CreditCard, BankAccount, Subscription
from Student.models import Property
from Accounts.models import Account


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