from django.contrib import admin
from .models import BlogArticle, ContactModelForm, Tool

# Register your models here.
admin.site.register(BlogArticle)
admin.site.register(ContactModelForm)
admin.site.register(Tool)