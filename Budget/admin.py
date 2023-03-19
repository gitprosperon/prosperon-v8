from django.contrib import admin
from .models import Goal, BudgetItems, BankAccount, MonthlySummary, BudgetUsers

admin.site.register(Goal)
admin.site.register(BudgetItems)
admin.site.register(BankAccount)
admin.site.register(MonthlySummary)
admin.site.register(BudgetUsers)