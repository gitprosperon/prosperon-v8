from django.contrib import admin
from .models import BlogArticle, ContactModelForm

# Register your models here.
admin.site.register(BlogArticle)
admin.site.register(ContactModelForm)