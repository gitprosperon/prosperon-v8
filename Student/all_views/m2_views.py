from django.shortcuts import render, redirect
from Student.forms import UpdateProgressForm, NewModuleSummaryForm
from Student.models import Student, Major, UniversityModule
from Accounts.models import Account



def budgeting_step1(request):
    user = request.user
    student_user = Account.objects.filter(pk=request.user.pk)
    user_id = student_user.model.get_user_id(self=user)
    student_model = Student.objects.get(user_id_number=user_id)

    if user.is_active and user.has_university == True:
        if request.method == 'POST':
            progress = request.POST['progress']
            if student_model.course_progress < progress:
                student_model.course_progress = progress
                student_model.save()
                return redirect('/university/video/6')
            else:
                return redirect('/university/video/6')

        return render(request, 'Students/m2-budgeting/step1.html')
    else:
        return render(request, 'MainWebsite/index.html')


def budgeting_step2(request):
    user = request.user
    student_user = Account.objects.filter(pk=request.user.pk)
    user_id = student_user.model.get_user_id(self=user)
    student_model = Student.objects.get(user_id_number=user_id)

    if user.is_active and user.has_university == True:
        if request.method == 'POST':
            progress = request.POST['progress']

            if student_model.course_progress < progress:

                module_summary_form = NewModuleSummaryForm(request.POST, request.FILES)
                newModule = module_summary_form.save(commit=False)
                newModule.user = request.user
                newModule.module_url = 'budgeting'
                newModule.module = UniversityModule.objects.get(module_title='Budgeting')
                newModule.users_id = user_id
                newModule.save()


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

    if user.is_active and user.has_university == True:
        if request.method == 'POST':
            progress = request.POST['progress']
            if student_model.course_progress < progress:
                student_model.course_progress = progress
                student_model.save()
                return redirect('/university/onboarding/step3')
            else:
                return redirect('/university/onboarding/step3')

        return render(request, 'Students/m2-budgeting/step3.html')
    else:
        return render(request, 'MainWebsite/index.html')
