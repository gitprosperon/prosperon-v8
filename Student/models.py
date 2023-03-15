from django.db import models
from django.conf import settings


# all different majors for jobs
class Major(models.Model):
    major_title = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.major_title


# All locations with associated apartment rent
class Location(models.Model):
    city = models.CharField(max_length=500, null=True, blank=True)
    average_rent = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.city


# All subscriptions
class Subscription(models.Model):
    subscription_title = models.CharField(max_length=250, null=True, blank=True)
    subscription_cost = models.FloatField(null=True, blank=True)
    subscription_id = models.CharField(max_length=250, null=True, blank=True)
    img = models.ImageField(upload_to='subscriptionImages/', null=True, blank=True)

    def __str__(self):
        return self.subscription_title + " - " + self.subscription_id


# Monthly expenses
class MonthlyExpense(models.Model):
    monthly_expense_title = models.CharField(max_length=250, null=True, blank=True)
    img = models.ImageField(upload_to='monthlyExpenseImages/', null=True, blank=True)
    RANGES = [
        ("$0-100", "$0-100"),
        ("$100-200", "$100-200"),
        ("$200-300", "$200-300"),
        ("$300-400", "$300-400"),
        ("$400-500", "$400-500"),
        ("$500-750", "$500-750"),
        ("$750-1000", "$750-1000"),
        ("$1000-1500", "$1000-1500"),
    ]
    monthly_expense_cost = models.IntegerField(null=True, blank=True, choices=RANGES)

    def __str__(self):
        return self.monthly_expense_title


# Models for get a job
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

    def __str__(self):
        return self.job_id + ' - ' + self.title


# Model for vehicles
class Vehicle(models.Model):
    vehicle_title = models.CharField(max_length=400, null=True, blank=True)


# Model for all fake apartments
class Apartment(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    sqFeet = models.CharField(max_length=500, null=True, blank=True)
    yearly_cost = models.IntegerField(null=True, blank=True)
    general_information = models.TextField(max_length=50000, null=True, blank=True)
    bedrooms = models.CharField(max_length=500, null=True, blank=True)
    bathrooms = models.CharField(max_length=500, null=True, blank=True)
    img = models.ImageField(upload_to='apartmentImages/', null=True, blank=True)
    initial_cost = models.IntegerField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)


# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    DTC = models.BooleanField(default=False, null=True, blank=True)
    student_email = models.CharField(max_length=200, null=True, blank=True)
    pilot = models.BooleanField(null=True, blank=True)
    user_id_number = models.CharField(max_length=250, null=True, blank=True)
    school = models.CharField(max_length=250, null=True, blank=True)
    class_code = models.CharField(max_length=250, null=True, blank=True)
    course_progress = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    age = models.CharField(max_length=200, null=True, blank=True)
    BIRTH_DAY_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31')
    ]
    birth_day = models.CharField(max_length=200, null=True, blank=True, choices=BIRTH_DAY_CHOICES)
    BIRTH_MONTH = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    ]
    birth_month = models.CharField(max_length=200, null=True, blank=True, choices=BIRTH_MONTH)
    BIRTH_YEAR_CHOICES = [
        ('1990', '1990'),
        ('1991', '1991'),
        ('1992', '1992'),
        ('1993', '1993'),
        ('1994', '1994'),
        ('1995', '1995'),
        ('1996', '1996'),
        ('1997', '1997'),
        ('1998', '1998'),
        ('1999', '1999'),
        ('2000', '2000'),
        ('2001', '2001'),
        ('2002', '2002'),
        ('2003', '2003'),
        ('2004', '2004'),
        ('2005', '2005'),
        ('2006', '2006'),
        ('2007', '2007'),
        ('2008', '2008'),
        ('2009', '2009'),
        ('2010', '2010'),
        ('2011', '2011'),
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023')
    ]
    birth_year = models.CharField(max_length=200, null=True, blank=True)


    YES_NO = [
        ("I Live With My Parents", "I Live With My Parents"),
        ("I Rent", "I Rent"),
        ("I Own", "I Own"),
    ]
    living_situation = models.CharField(max_length=2000, choices=YES_NO, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    desired_location = models.CharField(max_length=200, null=True, blank=True)

    GENDER_CHOICES = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Non-Binary', 'Non-Binary'),
        ('Not Specified', 'Not Specified'),
    )
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES, null=True, blank=True)
    ETHNICITY_CHOICES = (
        ('White', 'White'),
        ('Black or African American', 'Black or African American'),
        ('Hispanic or Latino', 'Hispanic or Latino'),
        ('American Indian or Alaska Native', 'American Indian or Alaska Native'),
        ('Asian', 'Asian'),
        ('Native Hawaiian or Other Pacific Islander', 'Native Hawaiian or Other Pacific Islander'),
        ('Multiracial/Other', 'Multiracial/Other'),
    )
    ethnicity = models.CharField(max_length=200, choices=ETHNICITY_CHOICES, null=True, blank=True)
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
    current_net_worth = models.IntegerField(null=True, blank=True)
    GRADUATION_DATES = (
        ('Spring 2023', 'Spring 2023'),
        ('Fall 2023', 'Fall 2023'),
        ('Spring 2024', 'Spring 2024'),
        ('Fall 2024', 'Fall 2024'),
        ('Spring 2025', 'Spring 2025'),
        ('Fall 2025', 'Fall 2025'),
        ('Spring 2026', 'Spring 2026'),
        ('Fall 2026', 'Fall 2026'),
    )
    graduation_date = models.CharField(max_length=200, null=True, blank=True, choices=GRADUATION_DATES)
    total_months_completed = models.IntegerField(null=True, blank=True)
    MONTHS = (
        ('1 ', 'January'),
        ('2', 'February'),
        ('3', 'March'),
        ('4', 'April'),
        ('5', 'May'),
        ('6', 'June'),
        ('7', 'July'),
        ('8', 'August'),
        ('9', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    )
    current_month = models.CharField(max_length=200, null=True, blank=True, choices=MONTHS)
    current_year = models.CharField(max_length=100000, null=True, blank=True)
    net_worth_monthly_list = models.JSONField(null=True, blank=True)
    completedAnytimeDecisions = models.CharField(max_length=400, null=True, blank=True)
    investing_activated = models.BooleanField(null=True, blank=True)
    apartments = models.ForeignKey(Apartment, on_delete=models.CASCADE, null=True, blank=True)
    properties = models.JSONField(null=True, blank=True)
    accounts = models.JSONField(null=True, blank=True)
    avaliable_scenarios = models.CharField(max_length=900, null=True, blank=True)
    scenario_display = models.CharField(max_length=200, null=True, blank=True)

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


# Properties
class Property(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    sqFeet = models.CharField(max_length=500, null=True, blank=True)
    yearly_cost = models.IntegerField(null=True, blank=True)
    general_information = models.TextField(max_length=500, null=True, blank=True)
    bedrooms = models.CharField(max_length=500, null=True, blank=True)
    bathrooms = models.CharField(max_length=500, null=True, blank=True)
    img = models.ImageField(upload_to='apartmentImages/', null=True, blank=True)
    total_cost = models.IntegerField(null=True, blank=True)
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


# Credit Cards
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


# Bank Accounts
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
        ('Miscellaneous', 'Miscellaneous'),
        ('Other', 'Other'),
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
    videos = models.JSONField(null=True, blank=True)
    module_results = models.JSONField(null=True, blank=True)
    back_btn = models.CharField(max_length=50000, null=True, blank=True)


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
    module_results = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.users_id + ' - ' + self.module_url


# Model for scenarios
class Scenario(models.Model):
    title = models.CharField(max_length=5000, null=True, blank=True)
    scenario_id = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=5000, null=True, blank=True)
    cost = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='scenarioImages/', null=True, blank=True)
    transaction_title = models.CharField(max_length=500, null=True, blank=True)
    scenario_category = models.CharField(max_length=500, null=True, blank=True, choices=BudgetItemsUniversity.CATAGORIES)

    def __str__(self):
        return self.scenario_id + ' - ' + self.title




