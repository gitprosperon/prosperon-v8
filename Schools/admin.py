from django.contrib import admin
from .models import School, Teacher, Classe

# Register your models here.
admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Classe)