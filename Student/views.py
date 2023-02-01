from django.shortcuts import render, redirect
from .models import video
from Accounts.models import Account
from Student.models import Student, ModuleSummarie, AnytimeDecision, BudgetItemsUniversity, Apartment, Job, UniversityModule
from .forms import AddBudgetForm, NewModuleSummaryForm
import json

# ------- UNIVERSITY MAIN VIEWS -----------

# University Dashboard
def dashboard(request):
    user = request.user


    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student_model = Student.objects.get(user_id_number=user_id)
        student_job_id = student_model.accepted_job

        first_name = student_model.first_name
        last_name = student_model.last_name
        profile_image = student_user.model.get_user_image(self=user)
        student_path = student_model.life_path['events']
        jobpicked = student_model.accepted_job



        if student_model.job is None:
            jobTitle = ''
        else:
            jobTitle = student_model.job.title


        if profile_image:
            pass
        else:
            profile_image = ''
        age = student_model.age
        location = student_model.location
        total_points = student_model.total_points
        last_points = student_model.last_points_added
        anytime_dec = AnytimeDecision.objects.all()



        context = {
            'first_name': first_name,
            'last_name': last_name,
            'profile_image': profile_image,
            'age': age,
            'anytime_dec': anytime_dec,
            'student_path': student_path,
            'jobTitle': jobTitle,
            'location': location,
            'total_points': total_points,
            'last_points': last_points
        }

        return render(request, 'Students/dashboard.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')


# Budget / Goals Page
def goals(request):

    return render(request, 'Students/budget/goals.html')

# Budget / Add Goals
def add_goals(request):

    return render(request, 'Students/budget/add_goal.html')


# Budget / Budget page
def budget(request):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student_model = Student.objects.get(user_id_number=user_id)
        user_university_budget_items = BudgetItemsUniversity.objects.filter(users_id=user_id)
        yearly_salary = student_model.yearly_salary
        monthly_salary = student_model.yearly_salary / 12
        monthly_salary = round(monthly_salary)

        context = {
            'user_university_budget_items': user_university_budget_items,
            'yearly_salary': yearly_salary,
            'monthly_salary': monthly_salary

        }
        return render(request, 'Students/budget/budget.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')


# Budget / Add budget
def add_budget(request):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student_model = Student.objects.get(user_id_number=user_id)

        if request.method == 'POST':
            print(request.POST)
            form = AddBudgetForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.users_id = user_id
                instance.save()
                return redirect('/university/budget/budget')
        else:
            form = AddBudgetForm(request.POST)


    context = {
        'form': form
    }
    return render(request, 'Students/budget/add_budget.html', context=context)

# Budget / transactions page
def transactions(request):
    return render(request, 'Students/budget/transactions.html')

# Universal Video Page
def universal_video(request, id):
    the_video = video.objects.get(id=id)
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        print(request.POST)
        if user.is_active:
            if request.method == 'POST':
                progress = request.POST['progress']
                next_btn = request.POST['next-button']
                student_model = Student.objects.get(user_id_number=user_id)
                print(student_model.course_progress)
                if student_model.course_progress < progress:
                    student_model.course_progress = progress
                    student_model.save()


                    return redirect(f'/{next_btn}')
                else:
                    return redirect(f'/{next_btn}')
            print(request.POST)


            context = {
                'video': the_video
            }
            return render(request, 'Students/uni-video.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')


# End of module summaries
def module_summaries(request, id, c):
    user = request.user
    if user.is_active and user.has_university == True:
        summary = ModuleSummarie.objects.get(user=user, module_url=id)
        print(summary)
        summary_title = summary.module.module_title
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student = Student.objects.get(user_id_number=user_id)
        next_module = summary.module.next_life_event['nextEvent']
        print(next_module['title'])

        # Defining page type for buttons on front end
        page_type = c

        # Getting max points for doing module
        student_total_points = student.total_points
        modulePoints = UniversityModule.objects.get(module_id=id).points
        total_points = student_total_points + modulePoints
        student.last_points_added = modulePoints
        student.total_points = total_points
        student.save()



        # Generating unlocked anytime decisions
        unlocked_decisions = UniversityModule.objects.get(module_id=id).unlocked_decisions
        unlocked_decisions = json.loads(unlocked_decisions)
        all_unlocked_decisions = []
        all_unlocked_decision_ids = []

        # Cleaning unlocked anytime decisions and putting them into new list
        for i in unlocked_decisions:
            decision = AnytimeDecision.objects.get(decision_id=i)
            all_unlocked_decisions.append(decision)
            all_unlocked_decision_ids.append(decision.decision_id)


        # Checking to see if there are any unlocked anytime decisions
        unlocked = student.unlocked_anytime_decisions

        if unlocked is None:
            student.unlocked_anytime_decisions = all_unlocked_decision_ids
            student.save()
        else:
            pass


        # appending upcoming life event to timeline
        if c == '0':
            decisions = []
            for decision in student.life_path['events']:
                decisions.append(decision['title'])

            if next_module['title'] in decisions:
                pass
            else:
                student.life_path['events'][-1]['status'] = "completed"
                student.total_points = total_points
                student.life_path['events'].append(next_module)
                student.save()



        context = {
            'summary': summary,
            'summary_title': summary_title,
            'page_type': page_type,
            'anytime_dec': all_unlocked_decisions,
            'modulePoints': modulePoints,
            'total_points': total_points

        }
        return render(request, 'Students/module_summary.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')

# all anytime decisions
def anytime_decision_bank(request):
    anytime_decisions = AnytimeDecision.objects.all()

    context = {
        "anytime_decisions": anytime_decisions
    }
    return render(request, 'Students/all_anytime_decisions.html', context=context)

# Specific Anytime Decision
def anytime_decision(request, id):
    ad = AnytimeDecision.objects.get(pk=id)

    context = {
        'ad': ad
    }
    return render(request, 'Students/anytime-decision.html', context=context)


def anytime_decision_step2(request, id):
    user = request.user
    if user.is_active and user.has_university == True:
        student_user = Account.objects.filter(pk=request.user.pk)
        user_id = student_user.model.get_user_id(self=user)
        student = Student.objects.get(user_id_number=user_id)
        ad = AnytimeDecision.objects.get(decision_id=id)
        html_path = ad.step2_path
        apartments = Apartment.objects.all()

        # Grabbing request
        if request.method == 'POST':
            print('there was a request')
            full_life_path = student.life_path['events']

            # removed object
            upcoming_module = student.life_path['events'][-1]
            del full_life_path[-1]

            # Adding anytime Decision
            anytime = {
                "title": f"{ad.title}",
                "type": "Anytime Decision",
                "description": f"{ad.description}",

            }

            full_life_path.append(anytime)
            full_life_path.append(upcoming_module)
            new = {"events": full_life_path}
            student.life_path = new
            student.save()
            return redirect('/university/dashboard')




        context = {
            'ad': ad,
            'id': id,
            'apartments': apartments
        }
        return render(request, f'Students/anytime-decisions/{html_path}', context=context)
    else:
        return render(request, 'MainWebsite/index.html')
