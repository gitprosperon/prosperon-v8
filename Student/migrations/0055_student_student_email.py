# Generated by Django 4.1.4 on 2023-01-30 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0054_apartment_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]