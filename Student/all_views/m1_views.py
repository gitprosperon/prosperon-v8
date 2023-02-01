import random

from django.shortcuts import render, redirect
from Student.forms import UpdateProgressForm
from Student.models import Student, Major, Job, ModuleSummarie, UniversityModule
from Accounts.models import Account
from Student.forms import NewModuleSummaryForm

def first_job_step1(request):
    user = request.user
    student_user = Account.objects.filter(pk=request.user.pk)
    user_id = student_user.model.get_user_id(self=user)
    student_model = Student.objects.get(user_id_number=user_id)
    all_jobs = Job.objects.all()
    print('request', request.POST)
    if user.is_active and user.has_university == True:
        if request.method == 'POST':
            jobs = request.POST['jobs']
            progress = request.POST['progress']
            if student_model.course_progress < progress:
                student_model.course_progress = progress
                student_model.jobs_applied = [jobs]
                print('jobs applied')
                print(student_model.jobs_applied)
                student_model.save()
                print('complete')
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
    jobs_applied = student_model.jobs_applied
    jobs_applied = jobs_applied.replace("'", "")
    print()

    if user.is_active and user.has_university == True:
        the_jobs = []
        jobs = Job.objects.all()
        for job in jobs:
            if job.job_id in jobs_applied:

                the_jobs.append(job)
                print(the_jobs)

        if request.method == 'POST':
            print(request.POST)
            progress = request.POST['progress']
            if student_model.course_progress < progress:
                student_model.course_progress = progress
                student_model.save()
                return redirect('/university/video/3')
            else:
                return redirect('/university/video/3')

        context = {
            'the_jobs': the_jobs
        }

        return render(request, 'Students/m1-first_job/step2.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')


def first_job_step3(request):
    user = request.user

    print('first job step 3')
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student_model = Student.objects.get(user_id_number=user_id)
        jobs_applied = student_model.jobs_applied
        jobs_applied = jobs_applied.replace("'", "")
        the_jobs = []
        jobs = Job.objects.all()
        for job in jobs:
            if job.job_id in jobs_applied:
                the_jobs.append(job)



        if request.method == 'POST':
            print(request.POST)
            progress = request.POST['progress']
            student_progress = int(student_model.course_progress)
            if student_progress < 10:
                student_model.course_progress = progress
                student_model.save()



                return redirect('/university/video/4')
            else:
                return redirect('/university/video/4')



        context = {
            'the_jobs': the_jobs[0:2]
        }

        return render(request, 'Students/m1-first_job/step3.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')



def first_job_step4(request):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student_model = Student.objects.get(user_id_number=user_id)
        jobs_applied = student_model.jobs_applied
        jobs_applied = jobs_applied.replace("'", "")

        the_jobs = []
        jobs = Job.objects.all()
        for job in jobs:
            if job.job_id in jobs_applied:
                the_jobs.append(job)
                print('the jobs',the_jobs)


        # Handling Request
        if request.method == 'POST':
            progress = request.POST['progress']
            progress = int(progress)
            studentProgress = int(student_model.course_progress)
            # Only updating if course progress meets requirement
            if studentProgress == 11:
                # Creating new module summary object

                module_summary_form = NewModuleSummaryForm(request.POST, request.FILES)
                newModule = module_summary_form.save(commit=False)
                newModule.user = request.user
                newModule.module_url = 'first_job'
                newModule.module = UniversityModule.objects.get(module_title='First Job')
                newModule.users_id = user_id
                newModule.save()

                acceptedJob = request.POST['accepted-job']
                student_model.accepted_job = acceptedJob
                student_job = Job.objects.get(job_id=acceptedJob)

                cleaned_salary = student_job.salary_range.replace('$', '')
                cleaned_salary = cleaned_salary.replace(',', '')
                cleaned_salary = cleaned_salary.partition('-')
                min = cleaned_salary[0]
                max = cleaned_salary[2]
                salary = random.randint(int(min), int(max))
                student_model.yearly_salary = salary


                student_model.course_progress = progress
                student_model.job = student_job
                student_model.save()
                return redirect('/university/module_summary/first_job/0')
            else:
                return redirect('/university/module_summary/first_job/0')

        context = {
            'the_jobs': the_jobs[0:2]
        }

        return render(request, 'Students/m1-first_job/step4.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')