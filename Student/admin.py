from django.contrib import admin
from .models import Student, Major, video, Job, AnytimeDecision, BudgetItemsUniversity, ModuleSummarie, UniversityModule, Apartment
from .models import Location, CreditCard, BankAccount, Subscription, MonthlyExpense

admin.site.register(Major)
admin.site.register(Student)
admin.site.register(video)
admin.site.register(Job)
admin.site.register(AnytimeDecision)
admin.site.register(BudgetItemsUniversity)
admin.site.register(UniversityModule)
admin.site.register(ModuleSummarie)
admin.site.register(Apartment)
admin.site.register(Location)
admin.site.register(CreditCard)
admin.site.register(BankAccount)
admin.site.register(Subscription)
admin.site.register(MonthlyExpense)

