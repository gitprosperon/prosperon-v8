# Generated by Django 4.1.4 on 2023-01-16 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0036_student_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
