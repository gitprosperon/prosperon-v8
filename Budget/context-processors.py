from Accounts.models import Account
from Student.models import Student
import datetime as dt


def account_info(request):
    user = request.user
    if user.is_active:
        account = Account.objects.filter(pk=request.user.pk)
        user_id = account.model.get_user_id(self=user)


        # Prosperon university things. Change later to be more efficient
        user_image = account.model.get_user_image(self=user)
        student = Student.objects.get(user_id_number=user_id)
        student_total_monthly_spending = student.total_monthly_expenses
        student_income = student.yearly_salary
        student_month = student.current_month
        student_year = student.current_year
        pilot = student.pilot
        first_name = student.first_name
        student_course_progress = int(student.course_progress)



        # Budget
        current_date = dt.date.today()
        month_name = current_date.strftime('%B').capitalize()
        current_year = current_date.year

        return {
            'first_name': first_name,
            'user_image': user_image,
            'student_total_monthly_spending': student_total_monthly_spending,
            'student_income': student_income,
            'student_month': student_month,
            'student_year': student_year,
            'pilot': pilot,
            'student_course_progress': student_course_progress,
            'month_name': month_name,
            'current_year': current_year
        }

    else:
        return {
            'first_name': 'user',
            'user_image': 'img',
        }