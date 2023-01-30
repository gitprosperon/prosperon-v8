from django.urls import path
from .all_views import m0_views, m1_views, m2_views
from Student import views
app_name = "Students"


urlpatterns = [
    # Sidebar Pages
    path('university/dashboard', views.dashboard, name='dashboard'),

    # Budgeting pages
    path('university/budget/goals', views.goals, name='goals'),
    path('university/budget/add-goals', views.add_goals, name='add-goals'),

    path('university/budget/budget', views.budget, name='budget'),
    path('university/budget/add_budget', views.add_budget, name='add-budget'),
    path('university/budget/transactions', views.transactions, name='transactions'),


    # Universal Video Page
    path('university/video/<str:id>', views.universal_video, name='universal-video-page'),

    # Module Summary
    path('university/module_summary/<str:id>/<str:type>', views.module_summaries, name='module-summary-page'),

    # Onboarding Urls
    path('university/onboarding/step1', m0_views.onboarding_step1, name='onboarding-step1'),
    path('university/onboarding/step2', m0_views.onboarding_step2, name='onboarding-step2'),
    path('university/onboarding/step3', m0_views.onboarding_step3, name='onboarding-step3'),
    path('university/onboarding/step4', m0_views.onboarding_step4, name='onboarding-step4'),


    # First Job Urls
    path('university/first-job/step1', m1_views.first_job_step1, name='first-job-step1'),
    path('university/first-job/step2', m1_views.first_job_step2, name='first-job-step2'),
    path('university/first-job/step3', m1_views.first_job_step3, name='first-job-step3'),
    path('university/first-job/step4', m1_views.first_job_step4, name='first-job-step4'),

    #Budgeting Urls
    path('university/budgeting/step1', m2_views.budgeting_step1, name='budgeting-step1'),
    path('university/budgeting/step2', m2_views.budgeting_step2, name='budgeting-step2'),
    path('university/budgeting/step3', m2_views.budgeting_step3, name='budgeting-step3'),

    #Goals Urls


]


