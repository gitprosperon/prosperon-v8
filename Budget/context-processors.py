from Accounts.models import Account
from Student.models import Student


def account_info(request):
    user = request.user
    if user.is_active:
        account = Account.objects.filter(pk=request.user.pk)
        user_id = account.model.get_user_id(self=user)
        first_name = account.model.get_first_name(self=user)
        user_image = account.model.get_user_image(self=user)
        student_total_monthly_spending = Student.objects.get(user_id_number=user_id).total_monthly_expenses
        student_income = Student.objects.get(user_id_number=user_id).yearly_salary
        student_month = Student.objects.get(user_id_number=user_id).current_month
        student_year = Student.objects.get(user_id_number=user_id).current_year


        if student_month == '4':
            print('it is wa')

        print('test')

        return {
            'first_name': first_name,
            'user_image': user_image,
            'student_total_monthly_spending': student_total_monthly_spending,
            'student_income': student_income,
            'student_month': student_month,
            'student_year': student_year
        }

    else:
        return {
            'first_name': 'user',
            'user_image': 'img',
        }