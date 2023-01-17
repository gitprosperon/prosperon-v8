from django.shortcuts import render, redirect
from .models import video
from Accounts.models import Account
from Student.models import Student, ModuleSummarie, AnytimeDecision

# ------- UNIVERSITY MAIN VIEWS -----------

# University Dashboard
def dashboard(request):
    user = request.user
    student_user = Account.objects.filter(pk=request.user.pk)
    user_id = student_user.model.get_user_id(self=user)
    student_model = Student.objects.get(user_id_number=user_id)

    if user.is_active and user.has_university == True:
        first_name = student_user.model.get_first_name(self=user)
        last_name = student_user.model.get_last_name(self=user)
        profile_image = student_user.model.get_user_image(self=user)
        if profile_image:
            pass
        else:
            profile_image = ''
        age = student_model.age
        anytime_dec = AnytimeDecision.objects.all()


        if request.method == 'POST':
            print(request.POST)
            progress = request.POST['progress']


        context = {
            'first_name': first_name,
            'last_name': last_name,
            'profile_image': profile_image,
            'age': age,
            'anytime_dec': anytime_dec,
        }

        return render(request, 'Students/dashboard.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')




# Budget / Goals Page
def goals(request):

    return render(request, 'Students/budget/goals.html')

def add_goals(request):

    return render(request, 'Students/budget/add_goal.html')


# Budget / Budget page
def budget(request):
    return render(request, 'Students/budget/budget.html')

# add budget
def add_budget(request):
    return render(request, 'Students/budget/add_budget.html')

# Budget / transactions page
def transactions(request):
    return render(request, 'Students/budget/transactions.html')

# Universal Video Page
def universal_video(request, id):
    the_video = video.objects.get(id=id)
    user = request.user
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

# End of module summaries
def module_summaries(request, id):
    user = request.user

    summary = ModuleSummarie.objects.get(user=user, module_url=id)
    summary_title = summary.module.module_title


    context = {
        'summary': summary,
        'summary_title': summary_title,

    }

    return render(request, 'Students/module_summary.html', context=context)

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

