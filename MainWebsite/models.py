from django.db import models

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