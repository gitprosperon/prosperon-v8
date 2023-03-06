import random

import humanize
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
    student_major = student_model.major
    all_jobs = Job.objects.filter(major=student_major)
    if user.is_active and user.has_university == True:
        if request.method == 'POST':
            jobs = request.POST['jobs']
            progress = request.POST['progress']
            if student_model.course_progress < progress:
                student_model.course_progress = progress
                student_model.jobs_applied = [jobs]
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
    graduation = student_model.graduation_date.replace("(", "")
    graduation = graduation.replace(")", "").replace("'", "").partition(",")[0].partition(" ")
    season = graduation[0]
    year = graduation[2]
    jobs_applied = student_model.jobs_applied
    jobs_applied = jobs_applied.replace("'", "")

    if user.is_active and user.has_university == True:
        the_jobs = []
        jobs = Job.objects.all()
        for job in jobs:
            if job.job_id in jobs_applied:
                the_jobs.append(job)

        if request.method == 'POST':
            progress = request.POST['progress']
            if student_model.course_progress < progress:
                student_model.course_progress = progress
                student_model.save()
                return redirect('/university/video/3')
            else:
                return redirect('/university/video/3')

        context = {
            'the_jobs': the_jobs[0:3],
            'graduation': graduation,
            'season': season,
            'year': year
        }
        return render(request, 'Students/m1-first_job/step2.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')


def first_job_step3(request):
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

        if request.method == 'POST':
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

                # For packaging module results



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

                # Grabbing the accepted job
                acceptedJob = request.POST['accepted-job']
                student_model.accepted_job = acceptedJob
                student_job = Job.objects.get(job_id=acceptedJob)

                # Cleaning salary range
                cleaned_salary = student_job.salary_range.replace('$', '')
                cleaned_salary = cleaned_salary.replace(',', '')
                cleaned_salary = cleaned_salary.partition('-')
                min = cleaned_salary[0]
                max = cleaned_salary[2]
                salary = random.randint(int(min), int(max))
                student_model.yearly_salary = salary

                # Packaging benefits into module results
                company_401k = student_job.company_401k
                health = ['health', student_job.health]
                dental = ['dental', student_job.dental]
                vision = ['vision', student_job.vision]
                pto = ['paid time off', student_job.pto]
                student_loan_assist = ['student loan assist', student_job.student_loan_assist]
                relocation = ['relocation', student_job.relocation]
                result_json = {"module_results": []}

                number = 13414
                print()

                packaged_salary = {"title": f"Monthly Salary: ${humanize.intcomma(round(salary/12))}"}
                result_json['module_results'].append(packaged_salary)



                benefits = [company_401k, health, dental, vision, pto, student_loan_assist, relocation]
                for benefit in benefits:
                    if benefit[1] == 'Yes':
                        packaged = {"title": benefit[0]}
                        result_json['module_results'].append(packaged)

                newModule.module_results = result_json
                newModule.save()

                # Adding course progress if needed
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