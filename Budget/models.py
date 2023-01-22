from django.db import models
from django.conf import settings


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
    CATAGORIES = [
        ('Food and Drink', 'Food and Drink'),
        ('Transportation', 'Transportation'),
        ('Shops', 'Shops'),
        ('Transfer', 'Transfer'),
        ('Service', 'Service'),
        ('Payment', 'Payment'),
        ('Income', 'Income'),

    ]
    category = models.CharField(max_length=200, null=True, blank=True, choices=CATAGORIES)
    total_per_month = models.IntegerField(null=True, blank=True)
    users_id = models.CharField(max_length=100, null=True, blank=True)



class BankAccount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    token = models.CharField(max_length=100, null=True, blank=True)
    users_id = models.CharField(max_length=100, null=True, blank=True)

    def getBankAccounts(self):
        return self.user


class MonthlySummary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    account_transactions = models.JSONField(null=True, blank=True)
    all_transactions = models.JSONField(null=True, blank=True)
    users_id = models.CharField(max_length=100, null=True, blank=True)
