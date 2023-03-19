from django.db import models
from django.conf import settings


# Budget Users
class BudgetUsers(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    users_id = models.CharField(max_length=100, null=True, blank=True)
    networth_timeline = models.JSONField(null=True, blank=True)
    checking_savings_total = models.FloatField(null=True, blank=True)
    credit_avaliable = models.FloatField(null=True, blank=True)
    investments = models.FloatField(null=True, blank=True)
    loans = models.FloatField(null=True, blank=True)
    real_estate = models.FloatField(null=True, blank=True)

    average_income = models.FloatField(null=True, blank=True)


# Goals
class Goal(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    cost = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='goalImages/')
    current_amount = models.IntegerField(null=True, blank=True)
    users_id = models.CharField(max_length=100, null=True, blank=True)
    icon = models.CharField(max_length=100, null=True, blank=True)

    CATAGORIES = [
        ('Food and Drink', 'Food and Drink'),
        ('Transportation', 'Transportation'),
        ('Shops', 'Shops'),
        ('Transfer', 'Transfer'),
        ('Service', 'Service'),
        ('Payment', 'Payment'),
        ('Income', 'Income'),

    ]
    category = models.CharField(max_length=100, null=True, blank=True, choices=CATAGORIES)





class BudgetItems(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    budget_id = models.CharField(max_length=100, null=True, blank=True)
    CATAGORIES = [
        ('Food and Drink', 'Food and Drink'),
        ('Transportation', 'Transportation'),
        ('Shops', 'Shops'),
        ('Transfer', 'Transfer'),
        ('Service', 'Service'),
        ('Payment', 'Payment'),
        ('Income', 'Income'),
        ('Subscription', 'Subscription'),
        ('Miscellaneous', 'Miscellaneous'),
        ('Other', 'Other'),
    ]
    category = models.CharField(max_length=200, null=True, blank=True, choices=CATAGORIES)
    total_per_month = models.IntegerField(null=True, blank=True)
    current_total = models.FloatField(null=True, blank=True)
    users_id = models.CharField(max_length=100, null=True, blank=True)
    transactions = models.JSONField(null=True, blank=True)



class BankAccount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    token = models.CharField(max_length=100, null=True, blank=True)
    users_id = models.CharField(max_length=100, null=True, blank=True)




class MonthlySummary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    account_transactions = models.JSONField(null=True, blank=True)
    all_transactions = models.JSONField(null=True, blank=True)
    users_id = models.CharField(max_length=100, null=True, blank=True)
