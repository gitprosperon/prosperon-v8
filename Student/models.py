import json

from django.db import models
from django.conf import settings


# all different majors for jobs
class Major(models.Model):
    major_title = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.major_title

class Location(models.Model):
    city = models.CharField(max_length=500, null=True, blank=True)
    average_rent = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.city



class Subscription(models.Model):
    subscription_title = models.CharField(max_length=250, null=True, blank=True)
    subscription_cost = models.IntegerField(null=True, blank=True)
    subscription_id = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self):
        return self.subscription_title + " - " + self.subscription_id

class MonthlyExpense(models.Model):
    monthly_expense_title = models.CharField(max_length=250, null=True, blank=True)

    RANGES = [
        ("$0-100", "$0-100"),
        ("$100-200", "$100-200"),

    ]

    monthly_expense_cost = models.IntegerField(null=True, blank=True, choices=RANGES)

    def __str__(self):
        return self.monthly_expense_title




#Models for get a job
class Job(models.Model):
    title = models.CharField(max_length=400, null=True, blank=True)
    company = models.CharField(max_length=400, null=True, blank=True)
    job_id = models.CharField(max_length=400, null=True, blank=True)
    location = models.CharField(max_length=400, null=True, blank=True)
    job_city = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    logo = models.ImageField(upload_to='jobimages/', null=True, blank=True)
    PAYRANGE = [
        ("$>10,000", "$>10,000"),
        ("$10,001-$25,000", "$10,001-$25,000"),
        ("$25,001-$40,000", "$25,001-$40,000"),
        ("$40,001-$55,000", "$40,001-$55,000"),
        ("$55,001-$70,000", "$55,001-$70,000"),
        ("$70,001-$85,000", "$70,001-$85,000"),
        ("$85,001-$100,000", "$85,001-$100,000"),
        ("$100,001-$120,000", "$100,001-$120,000"),
        ("$120,001-$140,000", "$120,001-$140,000"),
        ("$140,001-$160,000", "$140,001-$160,000"),
        ("$160,000+", "$160,000+"),
    ]
    salary_range = models.CharField(max_length=400, choices=PAYRANGE, blank=True)
    STYLES = [
        ("On-Site", "On-Site"),
        ("Hybrid", "Hybrid"),
        ("Remote", "Remote"),
    ]
    job_type = models.CharField(max_length=400, choices=STYLES, null=True, blank=True)
    HOURS = [
        ("Full Time", "Full Time"),
        ("Part Time", "Part Time"),
    ]
    job_hours = models.CharField(max_length=400, choices=HOURS, null=True, blank=True)
    STRUCTURE = [
        ("Salary + Bonus", "Salary + Bonus"),
        ("Salary + Stock Options", "Salary + Stock Options"),
        ("Salary", "Salary"),
        ("Hourly Wage + Overtime", "Hourly Wage + Overtime"),
        ("Salary + Commission", "Salary + Commission"),
        ("Commission Only", "Commission Only"),
        ("Fixed Contract", "Fixed Contract"),
    ]
    pay_structure = models.CharField(max_length=100, null=True, choices=STRUCTURE, blank=True)
    YES_NO = [
        ("Yes", "Yes"),
        ("No", "No"),
        ("Not Specified", "Not Specified"),
    ]
    company_401k = models.CharField(max_length=100, null=True, choices=YES_NO, blank=True)
    health = models.CharField(max_length=100, null=True, choices=YES_NO, blank=True)
    dental = models.CharField(max_length=100, null=True, choices=YES_NO, blank=True)
    vision = models.CharField(max_length=100, null=True, choices=YES_NO, blank=True)
    pto = models.CharField(max_length=100, null=True, choices=YES_NO, blank=True)
    student_loan_assist = models.CharField(max_length=100, null=True, choices=YES_NO, blank=True)
    relocation = models.CharField(max_length=100, null=True, choices=YES_NO, blank=True)

    company_requirements = models.TextField(max_length=10000, null=True, blank=True)
    company_qualifications = models.TextField(max_length=10000, null=True, blank=True)
    company_description = models.TextField(max_length=10000, null=True, blank=True)

    major = models.ForeignKey(Major, on_delete=models.CASCADE, null=True, blank=True)





# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    student_email = models.CharField(max_length=200, null=True, blank=True)
    user_id_number = models.CharField(max_length=250, null=True, blank=True)
    school = models.CharField(max_length=250, null=True, blank=True)
    class_code = models.CharField(max_length=250, null=True, blank=True)
    course_progress = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    age = models.CharField(max_length=20, null=True, blank=True)
    YES_NO = [
        ("Yes", "Yes"),
        ("No", "No"),

    ]
    live_with_parents = models.CharField(max_length=20, choices=YES_NO, null=True, blank=True)
    location = models.CharField(max_length=20, null=True, blank=True)

    GENDER_CHOICES = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Not Specified', 'Not Specified'),
    )
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
    ETHNICITY_CHOICES = (
        ('white', 'White'),
        ('black', 'Black or African American'),
        ('latin', 'Hispanic or Latino'),
        ('native american', 'American Indian or Alaska Native'),
        ('asian', 'Asian'),
        ('islander or hawaiian', 'Native Hawaiian or Other Pacific Islander'),
        ('other', 'Multiracial/Other'),
    )
    ethnicity = models.CharField(max_length=20, choices=ETHNICITY_CHOICES, null=True, blank=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, null=True, blank=True)
    jobs_applied = models.CharField(max_length=100, null=True, blank=True)
    accepted_job = models.CharField(max_length=100, null=True, blank=True)
    life_path = models.JSONField(null=True, blank=True)
    yearly_salary = models.IntegerField(null=True, blank=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)
    unlocked_anytime_decisions = models.CharField(max_length=100, null=True, blank=True)
    last_points_added = models.IntegerField(null=True, blank=True)
    total_points = models.IntegerField(null=True, blank=True)
    total_monthly_expenses = models.IntegerField(null=True, blank=True)
    all_transactions = models.JSONField(null=True, blank=True)
    monthly_transactions = models.JSONField(null=True, blank=True)
    spending_profile_monthly_payments = models.JSONField(null=True, blank=True)
    # 0 = spender
    # 1 = planner
    # 2 = frugal
    spender_type = models.CharField(max_length=100, null=True, blank=True)





    def __str__(self):
        return self.student_email + ' - ' + self.user_id_number


# Model for all video pages
class video(models.Model):
    title = models.CharField(max_length=400, null=True, blank=True)
    progress = models.CharField(max_length=400, null=True, blank=True)
    video_link = models.CharField(max_length=400, null=True, blank=True)
    back_button = models.CharField(max_length=400, null=True, blank=True)
    next_button = models.CharField(max_length=400, null=True, blank=True)
    video_id = models.CharField(max_length=400, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    page_type = models.CharField(max_length=200, null=True, blank=True)
    vocab = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)



    def __str__(self):
        return self.video_id + ' - ' + self.title


# Model for all fake apartments
class Apartment(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    sqFeet = models.CharField(max_length=500, null=True, blank=True)
    yearly_cost = models.IntegerField(null=True, blank=True)
    general_information = models.TextField(max_length=500, null=True, blank=True)
    bedrooms = models.CharField(max_length=500, null=True, blank=True)
    bathrooms = models.CharField(max_length=500, null=True, blank=True)
    img = models.ImageField(upload_to='apartmentImages/', null=True, blank=True)
    initial_cost = models.IntegerField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)




# Model for all anytime Decisions
class AnytimeDecision(models.Model):
    title = models.CharField(max_length=5000, null=True, blank=True)
    name_id = models.CharField(max_length=5000, null=True, blank=True)
    step2_path = models.CharField(max_length=5000, null=True, blank=True)
    video_link = models.CharField(max_length=5000, null=True, blank=True)
    decision_id = models.CharField(max_length=5000, null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
    learning_objectives = models.TextField(max_length=5000, null=True, blank=True)
    vocab = models.TextField(max_length=5000, null=True, blank=True)
    yearly_cost = models.IntegerField(null=True, blank=True)
    monthly_cost = models.IntegerField(null=True, blank=True)
    next_btn_link = models.CharField(max_length=5000, null=True, blank=True)
    back_btn_link = models.CharField(max_length=5000, null=True, blank=True)
    summary = models.TextField(max_length=5000, null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)

    img = models.ImageField(upload_to='anytimeImages/', null=True, blank=True)


    def __str__(self):
        return self.decision_id + ' - ' + self.title

class CreditCard(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    img = models.ImageField(upload_to='creditCardImages/', null=True, blank=True)
    score = models.CharField(max_length=500, null=True, blank=True)
    feature1 = models.CharField(max_length=500, null=True, blank=True)
    feature2 = models.CharField(max_length=500, null=True, blank=True)
    feature3 = models.CharField(max_length=500, null=True, blank=True)
    feature4 = models.CharField(max_length=500, null=True, blank=True)
    apr = models.CharField(max_length=500, null=True, blank=True)
    yearlyFee = models.CharField(max_length=500, null=True, blank=True)
    atmFee = models.CharField(max_length=500, null=True, blank=True)
    credit_card_descrption = models.CharField(max_length=500, null=True, blank=True)
    signup_fee = models.CharField(max_length=500, null=True, blank=True)

class BankAccount(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    bank_img = models.ImageField(upload_to='bankAccountImages/', null=True, blank=True)
    score = models.CharField(max_length=500, null=True, blank=True)
    apy = models.CharField(max_length=500, null=True, blank=True)
    bank_Yearly_Fee = models.CharField(max_length=500, null=True, blank=True)
    bank_ATM_Fee = models.CharField(max_length=500, null=True, blank=True)
    bank_Account_Description = models.CharField(max_length=500, null=True, blank=True)
    bank_feature1 = models.CharField(max_length=500, null=True, blank=True)
    bank_feature2 = models.CharField(max_length=500, null=True, blank=True)
    bank_feature3 = models.CharField(max_length=500, null=True, blank=True)
    bank_feature4 = models.CharField(max_length=500, null=True, blank=True)
    bank_signup_fee = models.CharField(max_length=500, null=True, blank=True)



# Model for all budgets
class BudgetItemsUniversity(models.Model):
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

    ]
    category = models.CharField(max_length=200, null=True, blank=True, choices=CATAGORIES)
    total_per_month = models.IntegerField(null=True, blank=True)
    current_total = models.FloatField(null=True, blank=True)
    users_id = models.CharField(max_length=100, null=True, blank=True)
    transactions = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.users_id + " - " + self.category


# Model for all Modules
class UniversityModule(models.Model):
    module_title = models.CharField(max_length=500, null=True, blank=True)
    module_id = models.CharField(max_length=500, null=True, blank=True)
    start_date = models.CharField(max_length=500, null=True, blank=True)
    end_date = models.CharField(max_length=500, null=True, blank=True)
    next_life_event = models.JSONField(null=True, blank=True)
    img = models.ImageField(upload_to='moduleImages/', null=True, blank=True)
    whats_happened = models.TextField(max_length=5000, null=True, blank=True)
    unlocked_decisions = models.CharField(max_length=50000, null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)




    def __str__(self):
        return self.module_title


# Model for module summaries
class ModuleSummarie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    users_id = models.CharField(max_length=100, null=True, blank=True)
    module = models.ForeignKey(UniversityModule, on_delete=models.CASCADE, null=True, blank=True)
    module_url = models.CharField(max_length=500, null=True, blank=True)
    what_happened = models.CharField(max_length=500, null=True, blank=True)
    unlocked_decisions = models.CharField(max_length=5000, null=True, blank=True)
    points_earned = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.users_id + ' - ' + self.module_url

