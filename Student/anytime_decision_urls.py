from django.urls import path
from Student import views
app_name = "Anytime"


urlpatterns = [
    # page with all anytime decisions on it
    path('all/', views.anytime_decision_bank, name='all-anytime-decisions'),
    path('<str:id>/', views.anytime_decision, name='anytime-decision'),

]