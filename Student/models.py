from django.db import models
from django.conf import settings


# all different majors for jobs
class Major(models.Model):
    major_title = models.CharField(max_length=500, null=True, blank=True)


    def __str__(self):
        return self.major_title


# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    user_id_number = models.CharField(max_length=250, null=True, blank=True)
    school = models.CharField(max_length=250, null=True, blank=True)
    class_code = models.CharField(max_length=250, null=True, blank=True)
    course_progress = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    age = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    ethnicity = models.CharField(max_length=20, null=True, blank=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, null=True, blank=True)
    jobs_applied = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user_id_number


# Model for all video pages
class video(models.Model):
    title = models.CharField(max_length=400, null=True, blank=True)
    progress = models.CharField(max_length=400, null=True, blank=True)
    video_link = models.CharField(max_length=400, null=True, blank=True)
    back_button = models.CharField(max_length=400, null=True, blank=True)
    next_button = models.CharField(max_length=400, null=True, blank=True)


#Models for get a job
class Job(models.Model):
    title = models.CharField(max_length=400, null=True, blank=True)
    company = models.CharField(max_length=400, null=True, blank=True)
    job_id = models.CharField(max_length=400, null=True, blank=True)
    location = models.CharField(max_length=400, null=True, blank=True)
    logo = models.ImageField(upload_to='jobimages/', null=True, blank=True)
    PAYRANGE = [
        ("$>10,000", "$>10,000"),
        ("$10,001-$25,000", "$10,001-$25,000"),
        ("25,001-$40,000", "$25,001-$40,000"),
        ("$40,001-$55,000", "$40,001-$55,000"),
        ("$55,001-$70,000", "$55,001-$70,000"),
        ("$70,001-$85,000", "$70,001-$85,000"),
        ("$85,001- $100,000", "$85,001- $100,000"),
        ("$100,001- $120,000", "$100,001- $120,000"),
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


# Model for all anytime Decisions
class AnytimeDecision(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    video_link = models.CharField(max_length=500, null=True, blank=True)
    decision_id = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)


    def __str__(self):
        return self.title


# Model for all budgets
class BudgetItemsUniversity(models.Model):
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


# Model for all Modules
class UniversityModule(models.Model):
    module_title = models.CharField(max_length=500, null=True, blank=True)
    start_date = models.CharField(max_length=500, null=True, blank=True)
    end_date = models.CharField(max_length=500, null=True, blank=True)

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