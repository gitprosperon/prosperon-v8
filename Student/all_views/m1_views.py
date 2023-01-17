from django.shortcuts import render, redirect
from Student.forms import UpdateProgressForm
from Student.models import Student, Major, Job
from Accounts.models import Account

def first_job_step1(request):
    user = request.user
    student_user = Account.objects.filter(pk=request.user.pk)
    user_id = student_user.model.get_user_id(self=user)
    student_model = Student.objects.get(user_id_number=user_id)
    all_jobs = Job.objects.all()
    if user.is_active and user.has_university == True:
        if request.method == 'POST':
            jobs = request.POST['jobs']
            progress = request.POST['progress']
            if student_model.course_progress < progress:
                student_model.course_progress = progress
                student_model.jobs_applied = jobs
                student_model.save()
                return redirect('/university/video/2')
            else:
                return redirect('/university/video/2')

        context = {
            'all_jobs': all_jobs
        }

        return render(request, 'Students/m1-first_job/step1.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')



def first_job_step2(request):
    user = request.user
    student_user = Account.objects.filter(pk=request.user.pk)
    user_id = student_user.model.get_user_id(self=user)
    student_model = Student.objects.get(user_id_number=user_id)

    if user.is_active and user.has_university == True:
        if request.method == 'POST':
            print(request.POST)
            progress = request.POST['progress']
            if student_model.course_progress < progress:
                student_model.course_progress = progress
                student_model.save()
                return redirect('/university/video/3')
            else:
                return redirect('/university/video/3')

        return render(request, 'Students/m1-first_job/step2.html')
    else:
        return render(request, 'MainWebsite/index.html')


def first_job_step3(request):
    user = request.user
    student_user = Account.objects.filter(pk=request.user.pk)
    user_id = student_user.model.get_user_id(self=user)
    student_model = Student.objects.get(user_id_number=user_id)

    if user.is_active and user.has_university == True:
        if request.method == 'POST':
            print(request.POST)
            progress = request.POST['progress']
            if student_model.course_progress < progress:
                student_model.course_progress = progress
                student_model.save()
                return redirect('/university/video/4')
            else:
                return redirect('/university/video/4')

        return render(request, 'Students/m1-first_job/step3.html')
    else:
        return render(request, 'MainWebsite/index.html')




def first_job_step4(request):
    user = request.user
    student_user = Account.objects.filter(pk=request.user.pk)
    user_id = student_user.model.get_user_id(self=user)
    student_model = Student.objects.get(user_id_number=user_id)

    if user.is_active and user.has_university == True:
        if request.method == 'POST':
            print(request.POST)
            progress = request.POST['progress']
            if student_model.course_progress < progress:
                student_model.course_progress = progress
                student_model.save()
                return redirect('/university/module_summary/first_job')
            else:
                return redirect('/university/module_summary/first_job')

        return render(request, 'Students/m1-first_job/step4.html')
    else:
        return render(request, 'MainWebsite/index.html')