from django.db import models


# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=255, null=True, blank=True)
    number_of_students = models.IntegerField()
    access_token = models.CharField(max_length=12, null=True, blank=True)
    school_email_at = models.CharField(max_length=50, blank=True, null=True)
    school_image = models.ImageField(upload_to='schoolImages/', blank=True)

    def __str__(self):
        return self.school_name


class Teacher(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    access_token = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return self.email


class Classe(models.Model):
    class_name = models.CharField(max_length=255, null=True, blank=True)
    professor = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    class_code = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.professor.email