from django.db import models
from django.utils import timezone

# Create your models here.
class BlogArticle(models.Model):
    blog_title = models.CharField(max_length=500, null=True, blank=True)
    blog_image = models.ImageField(upload_to='blogImages/', null=True, blank=True)
    PAGETYPES = [
        ("blog_page_1", "blog_page_1"),
        ("blog_page_2", "blog_page_2"),
    ]
    page_type = models.CharField(max_length=500, null=True, blank=True, choices=PAGETYPES)
    blog_id = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    section_1_title = models.CharField(max_length=500, null=True, blank=True)
    section_1_content = models.TextField(null=True, blank=True)
    section_2_title = models.CharField(max_length=500, null=True, blank=True)
    section_2_content = models.TextField(null=True, blank=True)
    section_3_title = models.CharField(max_length=500, null=True, blank=True)
    section_3_content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.blog_title + ' - ' + self.blog_id


class ContactModelForm(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.email + ' - ' + f'{self.date.date()}'

class Tool(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    html_path = models.CharField(max_length=500, null=True, blank=True)
    tool_id = models.CharField(max_length=5000, null=True, blank=True)



