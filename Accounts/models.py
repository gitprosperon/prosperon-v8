from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError('users must have an email')
        if not username:
            raise ValueError('users must have a usernanme')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class Ethnicitie(models.Model):
    title = models.CharField(max_length=30, blank=True , null=True)

    def __str__(self):
        return self.title



class Account(AbstractBaseUser):
    # Basic Setup Information
    email = models.EmailField(verbose_name='email', max_length=30, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_blacklisted = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


    # all other information
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name


    user_id = models.CharField(max_length=12, null=True, blank=True)

    def get_user_id(self):
        return self.user_id

    has_university = models.BooleanField(default=False)
    has_budget = models.BooleanField(default=False)

    def check_if_budget(self):
        return self.has_budget

    user_image = models.ImageField(null=True, blank=True, upload_to='user_images/')

    def get_user_image(self):
        return self.user_image